; BigFloat implementation in Toy Assembly
; Translated from Python floatlib.py
;
; Global configuration (stored in memory starting at address 0):
;   [bx+0] = DIGITS_PER_ELEMENT = 7  (where bx=0)
;   [bx+1] = BASE = 10^7 = 10,000,000
;   [bx+2] = PRECISION = 16
;
; BigFloat structure (18 cells):
;   [ax+0]  = sign (1 or -1)      (where ax = base address)
;   [ax+1]  = exponent
;   [ax+2]  = values[0] (most significant)
;   [ax+3]  = values[1]
;   ...
;   [ax+17] = values[15] (least significant)
;   Total precision: 16 * 7 = 112 decimal digits

    jmp _start

; ============================================================
; Startup: Initialize global configuration
; ============================================================
_start:
    ; Use bx=0 as base for global config
    mov bx, 0

    ; DIGITS_PER_ELEMENT = 7
    mov ax, 7
    mov [bx+0], ax

    ; Calculate BASE = 10^7
    ; We'll compute 10^7 by repeated multiplication
    mov cx, 7          ; exponent counter
    mov ax, 1          ; result accumulator

_calc_base_loop:
    cmp cx, 0
    je _calc_base_done
    mul 10             ; ax = ax * 10
    sub cx, 1
    jmp _calc_base_loop

_calc_base_done:
    mov [bx+1], ax     ; BASE = 10,000,000

    ; PRECISION = 16 (so BigFloat = 2 + 16 = 18 cells, 16*7=112 digits precision)
    mov ax, 16
    mov [bx+2], ax

    ; Now jump to main program
    jmp main

; ============================================================
; _init_bigfloat: Initialize a BigFloat from an integer
;
; Stack frame:
;   [bp+5] = address where to create BigFloat
;   [bp+4] = initial integer value
;   [bp+3] = (return value slot - not used, returns nothing)
;   [bp+2] = saved ip (by call)
;   [bp+1] = saved bp
;   [bp+0] = current available stack space
;
; Caller convention:
;   push addr
;   push value
;   sub sp, 1        ; return value slot
;   call _init_bigfloat
;   add sp, 3        ; clean up
; ============================================================
_init_bigfloat:
    push bp
    mov bp, sp

    ; Get parameters
    mov ax, [bp+5]   ; address (use ax as base register for BigFloat)
    mov bx, [bp+4]   ; initial value

    ; Determine sign and store
    cmp bx, 0
    jge _init_positive

    ; Negative case: sign = -1, value = -value
    mov [ax+0], -1   ; sign = -1
    mov cx, 0
    sub cx, bx       ; cx = -bx (absolute value)
    mov bx, cx
    jmp _init_store_value

_init_positive:
    ; Positive case: sign = 1
    mov [ax+0], 1   ; sign = 1

_init_store_value:
    ; exponent = 0
    mov cx, 0
    mov [ax+1], cx

    ; values[0] = abs(initial value)
    mov [ax+2], bx

    ; Initialize values[1..15] to 0
    mov cx, 1
_init_zeros:
    mov ax, [bp+5]   ; BigFloat base addr
    add ax, 2        ; values addr
    add ax, cx       ; &values[i]
    mov [ax], 0
    add cx, 1
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp cx, dx
    jl _init_zeros

    ; Call normalize
    mov ax, [bp+5]   ; BigFloat address
    push ax
    sub sp, 1        ; return value slot
    call _normalize
    add sp, 2

    ; Restore stack frame and return
    mov sp, bp
    pop bp
    ret

; ============================================================
; _normalize: Normalize a BigFloat representation
;
; Handles carries, borrows, overflow, sign flip, and left shift
;
; Stack frame:
;   [bp+4] = BigFloat address
;   [bp+3] = (return value slot - not used)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;   [bp-1] = local: temp value
;   [bp-2] = local: carry/borrow
;
; Caller convention:
;   push addr
;   sub sp, 1
;   call _normalize
;   add sp, 2
; ============================================================
_normalize:
    push bp
    mov bp, sp
    sub sp, 3        ; 3 local variables

    ; --------------------------------------------------------
    ; Part 1: Handle carries from right to left
    ; for i = PRECISION-1 down to 1
    ; --------------------------------------------------------
    mov ax, 0
    mov ax, [ax+2]   ; PRECISION
    sub ax, 1        ; i = PRECISION - 1
    mov [bp+0], ax

_norm_carry_loop:
    mov ax, [bp+0]   ; i
    cmp ax, 1
    jl _norm_carry_done

    ; Load values[i]
    mov bx, [bp+4]   ; BigFloat addr
    add bx, 2        ; &values[0]
    add bx, ax       ; &values[i]
    mov cx, [bx]     ; cx = values[i]

    ; Check if values[i] >= BASE
    mov dx, 0
    mov ax, [dx+1]   ; BASE
    cmp cx, ax
    jl _norm_check_negative

    ; values[i] >= BASE: handle carry
    ; carry = values[i] / BASE
    ; values[i] = values[i] % BASE
    mov ax, cx       ; ax = values[i]
    mov dx, 0
    mov dx, [dx+1]   ; dx = BASE
    div dx           ; ax = quotient, dx = remainder
    mov [bp-2], ax   ; carry = quotient
    mov [bx], dx     ; values[i] = remainder

    ; values[i-1] += carry
    mov ax, [bp+0]   ; i
    sub ax, 1        ; i-1
    mov bx, [bp+4]   ; BigFloat addr
    add bx, 2
    add bx, ax       ; &values[i-1]
    mov cx, [bx]     ; values[i-1]
    add cx, [bp-2]   ; + carry
    mov [bx], cx
    jmp _norm_carry_next

_norm_check_negative:
    ; Check if values[i] < 0
    cmp cx, 0
    jge _norm_carry_next

    ; values[i] < 0: handle borrow
    ; borrow = (-values[i] + BASE - 1) / BASE
    mov ax, 0
    sub ax, cx       ; ax = -values[i]
    mov dx, 0
    mov dx, [dx+1]   ; BASE
    add ax, dx       ; + BASE
    sub ax, 1        ; - 1
    div dx           ; ax = borrow
    mov [bp-2], ax

    ; values[i] += borrow * BASE
    mov dx, 0
    mov dx, [dx+1]   ; BASE
    mul dx           ; ax = borrow * BASE
    add cx, ax       ; values[i] + borrow * BASE
    mov [bx], cx

    ; values[i-1] -= borrow
    mov ax, [bp+0]   ; i
    sub ax, 1        ; i-1
    mov bx, [bp+4]   ; BigFloat addr
    add bx, 2
    add bx, ax       ; &values[i-1]
    mov cx, [bx]
    sub cx, [bp-2]   ; - borrow
    mov [bx], cx

_norm_carry_next:
    mov ax, [bp+0]
    sub ax, 1
    mov [bp+0], ax
    jmp _norm_carry_loop

_norm_carry_done:
    ; --------------------------------------------------------
    ; Part 2: Handle overflow at values[0]
    ; if values[0] >= BASE
    ; --------------------------------------------------------
    mov bx, [bp+4]   ; BigFloat addr
    add bx, 2        ; &values[0]
    mov cx, [bx]     ; values[0]

    mov dx, 0
    mov ax, [dx+1]   ; BASE
    cmp cx, ax
    jl _norm_check_sign

    ; Overflow: shift right and increment exponent
    ; carry = values[0] / BASE
    mov ax, cx
    mov dx, 0
    mov dx, [dx+1]
    div dx           ; ax = carry, dx = remainder
    mov [bp-2], ax   ; save carry
    mov [bp-1], dx   ; save remainder for values[1]

    ; Shift values right: for i = PRECISION-1 down to 1
    mov ax, 0
    mov ax, [ax+2]   ; PRECISION
    sub ax, 1
    mov [bp+0], ax   ; i = PRECISION-1

_norm_shift_right:
    mov ax, [bp+0]
    cmp ax, 1
    jl _norm_shift_right_done

    ; values[i] = values[i-1]
    mov bx, [bp+4]
    add bx, 2
    add bx, ax       ; &values[i]
    mov cx, ax
    sub cx, 1        ; i-1
    mov dx, [bp+4]
    add dx, 2
    add dx, cx       ; &values[i-1]
    mov cx, [dx]     ; values[i-1]
    mov [bx], cx     ; values[i] = values[i-1]

    mov ax, [bp+0]
    sub ax, 1
    mov [bp+0], ax
    jmp _norm_shift_right

_norm_shift_right_done:
    ; values[0] = carry
    mov bx, [bp+4]
    add bx, 2
    mov ax, [bp-2]
    mov [bx], ax

    ; values[1] = values[1] % BASE (use saved remainder)
    mov bx, [bp+4]
    add bx, 3        ; &values[1]
    mov ax, [bp-1]
    mov [bx], ax

    ; exponent += 1
    mov bx, [bp+4]
    add bx, 1        ; &exponent
    mov ax, [bx]
    add ax, 1
    mov [bx], ax

_norm_check_sign:
    ; --------------------------------------------------------
    ; Part 3: Handle sign flip if values[0] < 0
    ; --------------------------------------------------------
    mov bx, [bp+4]
    add bx, 2
    mov ax, [bx]     ; values[0]
    cmp ax, 0
    jge _norm_shift_left_start

    ; Flip sign
    mov bx, [bp+4]   ; &sign
    mov ax, [bx]
    mov cx, 0
    sub cx, ax       ; -sign
    mov [bx], cx

    ; Negate all values: for i = 0 to PRECISION-1
    mov cx, 0
    mov [bp+0], cx

_norm_negate_loop:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _norm_negate_done

    ; values[i] = -values[i]
    mov bx, [bp+4]
    add bx, 2
    add bx, ax
    mov cx, [bx]
    mov dx, 0
    sub dx, cx
    mov [bx], dx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _norm_negate_loop

_norm_negate_done:
    ; Recurse to handle the flip
    mov ax, [bp+4]
    push ax
    sub sp, 1
    call _normalize
    add sp, 2
    jmp _norm_done

_norm_shift_left_start:
    ; --------------------------------------------------------
    ; Part 4: Shift left while values[0] == 0 and not all zeros
    ; --------------------------------------------------------
_norm_shift_left_check:
    ; Check if values[0] == 0
    mov bx, [bp+4]
    add bx, 2
    mov ax, [bx]
    cmp ax, 0
    jne _norm_done

    ; Check if any values[1..] != 0
    mov cx, 1
    mov [bp+0], cx

_norm_check_nonzero:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _norm_done   ; All zeros, we're done

    mov bx, [bp+4]
    add bx, 2
    add bx, ax
    mov cx, [bx]
    cmp cx, 0
    jne _norm_do_shift_left  ; Found non-zero, do shift

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _norm_check_nonzero

_norm_do_shift_left:
    ; Shift left: for i = 0 to PRECISION-2
    mov cx, 0
    mov [bp+0], cx

_norm_shift_left_loop:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    sub dx, 1        ; PRECISION - 1
    cmp ax, dx
    jge _norm_shift_left_loop_done

    ; values[i] = values[i+1]
    mov bx, [bp+4]
    add bx, 2
    add bx, ax       ; &values[i]
    mov cx, ax
    add cx, 1        ; i+1
    mov dx, [bp+4]
    add dx, 2
    add dx, cx       ; &values[i+1]
    mov cx, [dx]
    mov [bx], cx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _norm_shift_left_loop

_norm_shift_left_loop_done:
    ; values[PRECISION-1] = 0
    mov dx, 0
    mov ax, [dx+2]   ; PRECISION
    sub ax, 1
    mov bx, [bp+4]
    add bx, 2
    add bx, ax
    mov cx, 0
    mov [bx], cx

    ; exponent -= 1
    mov bx, [bp+4]
    add bx, 1        ; &exponent
    mov ax, [bx]
    sub ax, 1
    mov [bx], ax

    ; Continue checking
    jmp _norm_shift_left_check

_norm_done:
    mov sp, bp
    pop bp
    ret

; ============================================================
; _add_bigfloat: Add two BigFloat numbers
;
; result = a + b
;
; Stack frame:
;   [bp+6] = result address
;   [bp+5] = a address (first operand)
;   [bp+4] = b address (second operand)
;   [bp+3] = (return value slot - not used)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;   [bp-1] = local: exp_diff
;   [bp-2] = local: temp
;
; Caller convention:
;   push result_addr
;   push a_addr
;   push b_addr
;   sub sp, 1
;   call _add_bigfloat
;   add sp, 4
; ============================================================
_add_bigfloat:
    push bp
    mov bp, sp
    sub sp, 3        ; 3 local variables

    ; Calculate exp_diff = a.exponent - b.exponent
    mov ax, [bp+5]   ; a addr
    add ax, 1        ; &a.exponent
    mov bx, [ax]     ; a.exponent
    mov ax, [bp+4]   ; b addr
    add ax, 1        ; &b.exponent
    mov cx, [ax]     ; b.exponent
    sub bx, cx       ; exp_diff = a.exp - b.exp
    mov [bp-1], bx

    ; Branch based on exp_diff
    cmp bx, 0
    je _add_same_exp
    jg _add_a_larger_exp
    jmp _add_b_larger_exp

; --------------------------------------------------------
; Case 1: exp_diff == 0 (same exponent)
; --------------------------------------------------------
_add_same_exp:
    ; result.exponent = a.exponent
    mov ax, [bp+5]   ; a addr
    add ax, 1
    mov bx, [ax]     ; a.exponent
    mov ax, [bp+6]   ; result addr
    add ax, 1
    mov [ax], bx

    ; Check if signs are the same
    mov ax, [bp+5]   ; a addr
    mov bx, [ax]     ; a.sign
    mov ax, [bp+4]   ; b addr
    mov cx, [ax]     ; b.sign
    cmp bx, cx
    jne _add_same_exp_diff_sign

    ; Same sign: result.sign = a.sign, result.values[i] = a.values[i] + b.values[i]
    mov ax, [bp+6]   ; result addr
    mov [ax], bx     ; result.sign = a.sign

    ; Loop: for i = 0 to PRECISION-1
    mov cx, 0
    mov [bp+0], cx

_add_same_exp_same_sign_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _add_done_normalize

    ; result.values[i] = a.values[i] + b.values[i]
    mov bx, [bp+5]   ; a addr
    add bx, 2
    add bx, ax       ; &a.values[i]
    mov cx, [bx]     ; a.values[i]

    mov bx, [bp+4]   ; b addr
    add bx, 2
    add bx, ax       ; &b.values[i]
    mov dx, [bx]     ; b.values[i]
    add cx, dx       ; a.values[i] + b.values[i]

    mov bx, [bp+6]   ; result addr
    add bx, 2
    add bx, ax       ; &result.values[i]
    mov [bx], cx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _add_same_exp_same_sign_loop

_add_same_exp_diff_sign:
    ; Different sign: result.sign = a.sign, result.values[i] = a.values[i] - b.values[i]
    mov ax, [bp+6]   ; result addr
    mov [ax], bx     ; result.sign = a.sign

    ; Loop: for i = 0 to PRECISION-1
    mov cx, 0
    mov [bp+0], cx

_add_same_exp_diff_sign_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _add_done_normalize

    ; result.values[i] = a.values[i] - b.values[i]
    mov bx, [bp+5]   ; a addr
    add bx, 2
    add bx, ax       ; &a.values[i]
    mov cx, [bx]     ; a.values[i]

    mov bx, [bp+4]   ; b addr
    add bx, 2
    add bx, ax       ; &b.values[i]
    mov dx, [bx]     ; b.values[i]
    sub cx, dx       ; a.values[i] - b.values[i]

    mov bx, [bp+6]   ; result addr
    add bx, 2
    add bx, ax       ; &result.values[i]
    mov [bx], cx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _add_same_exp_diff_sign_loop

; --------------------------------------------------------
; Case 2: exp_diff > 0 (a has larger exponent)
; --------------------------------------------------------
_add_a_larger_exp:
    ; result.exponent = a.exponent
    mov ax, [bp+5]   ; a addr
    add ax, 1
    mov bx, [ax]     ; a.exponent
    mov ax, [bp+6]   ; result addr
    add ax, 1
    mov [ax], bx

    ; result.sign = a.sign
    mov ax, [bp+5]   ; a addr
    mov bx, [ax]     ; a.sign
    mov ax, [bp+6]   ; result addr
    mov [ax], bx

    ; Copy a.values to result.values
    mov cx, 0
    mov [bp+0], cx

_add_a_larger_copy_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _add_a_larger_add_shifted

    mov bx, [bp+5]   ; a addr
    add bx, 2
    add bx, ax
    mov cx, [bx]     ; a.values[i]

    mov bx, [bp+6]   ; result addr
    add bx, 2
    add bx, ax
    mov [bx], cx     ; result.values[i] = a.values[i]

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _add_a_larger_copy_loop

_add_a_larger_add_shifted:
    ; Add b.values at shifted positions
    ; for i = 0 to PRECISION-1: if i + exp_diff < PRECISION, add/sub
    mov cx, 0
    mov [bp+0], cx

_add_a_larger_shift_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _add_done_normalize

    ; Check if i + exp_diff < PRECISION
    mov bx, ax
    add bx, [bp-1]   ; i + exp_diff
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp bx, dx
    jge _add_a_larger_shift_next

    ; Check if same sign
    mov cx, [bp+5]   ; a addr
    mov cx, [cx]     ; a.sign
    mov dx, [bp+4]   ; b addr
    mov dx, [dx]     ; b.sign
    cmp cx, dx
    jne _add_a_larger_shift_sub

    ; Same sign: result.values[i + exp_diff] += b.values[i]
    mov cx, [bp+4]   ; b addr
    add cx, 2
    add cx, ax       ; &b.values[i]
    mov dx, [cx]     ; b.values[i]

    mov cx, [bp+6]   ; result addr
    add cx, 2
    add cx, bx       ; &result.values[i + exp_diff]
    mov ax, [cx]
    add ax, dx
    mov [cx], ax
    jmp _add_a_larger_shift_next

_add_a_larger_shift_sub:
    ; Different sign: result.values[i + exp_diff] -= b.values[i]
    mov cx, [bp+4]   ; b addr
    add cx, 2
    mov dx, [bp+0]   ; i
    add cx, dx       ; &b.values[i]
    mov dx, [cx]     ; b.values[i]

    mov cx, [bp+6]   ; result addr
    add cx, 2
    add cx, bx       ; &result.values[i + exp_diff]
    mov ax, [cx]
    sub ax, dx
    mov [cx], ax

_add_a_larger_shift_next:
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _add_a_larger_shift_loop

; --------------------------------------------------------
; Case 3: exp_diff < 0 (b has larger exponent)
; --------------------------------------------------------
_add_b_larger_exp:
    ; result.exponent = b.exponent
    mov ax, [bp+4]   ; b addr
    add ax, 1
    mov bx, [ax]     ; b.exponent
    mov ax, [bp+6]   ; result addr
    add ax, 1
    mov [ax], bx

    ; result.sign = b.sign
    mov ax, [bp+4]   ; b addr
    mov bx, [ax]     ; b.sign
    mov ax, [bp+6]   ; result addr
    mov [ax], bx

    ; Copy b.values to result.values
    mov cx, 0
    mov [bp+0], cx

_add_b_larger_copy_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _add_b_larger_add_shifted

    mov bx, [bp+4]   ; b addr
    add bx, 2
    add bx, ax
    mov cx, [bx]     ; b.values[i]

    mov bx, [bp+6]   ; result addr
    add bx, 2
    add bx, ax
    mov [bx], cx     ; result.values[i] = b.values[i]

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _add_b_larger_copy_loop

_add_b_larger_add_shifted:
    ; Add a.values at shifted positions
    ; exp_diff is negative, so we use i - exp_diff = i + |exp_diff|
    ; for i = 0 to PRECISION-1: if i - exp_diff < PRECISION, add/sub
    mov cx, 0
    mov [bp+0], cx

_add_b_larger_shift_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _add_done_normalize

    ; Check if i - exp_diff < PRECISION
    ; exp_diff is negative, so i - exp_diff = i + |exp_diff|
    mov bx, ax
    sub bx, [bp-1]   ; i - exp_diff (since exp_diff < 0, this adds)
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp bx, dx
    jge _add_b_larger_shift_next

    ; Check if same sign
    mov cx, [bp+5]   ; a addr
    mov cx, [cx]     ; a.sign
    mov dx, [bp+4]   ; b addr
    mov dx, [dx]     ; b.sign
    cmp cx, dx
    jne _add_b_larger_shift_sub

    ; Same sign: result.values[i - exp_diff] += a.values[i]
    mov cx, [bp+5]   ; a addr
    add cx, 2
    add cx, ax       ; &a.values[i]
    mov dx, [cx]     ; a.values[i]

    mov cx, [bp+6]   ; result addr
    add cx, 2
    add cx, bx       ; &result.values[i - exp_diff]
    mov ax, [cx]
    add ax, dx
    mov [cx], ax
    jmp _add_b_larger_shift_next

_add_b_larger_shift_sub:
    ; Different sign: result.values[i - exp_diff] -= a.values[i]
    mov cx, [bp+5]   ; a addr
    add cx, 2
    mov dx, [bp+0]   ; i
    add cx, dx       ; &a.values[i]
    mov dx, [cx]     ; a.values[i]

    mov cx, [bp+6]   ; result addr
    add cx, 2
    add cx, bx       ; &result.values[i - exp_diff]
    mov ax, [cx]
    sub ax, dx
    mov [cx], ax

_add_b_larger_shift_next:
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _add_b_larger_shift_loop

; --------------------------------------------------------
; Normalize result and return
; --------------------------------------------------------
_add_done_normalize:
    mov ax, [bp+6]   ; result addr
    push ax
    sub sp, 1
    call _normalize
    add sp, 2

    mov sp, bp
    pop bp
    ret

; ============================================================
; _sub_bigfloat: Subtract two BigFloat numbers
;
; result = a - b
;
; Implementation: negate b's sign, call add, restore b's sign
;
; Stack frame:
;   [bp+6] = result address
;   [bp+5] = a address (first operand)
;   [bp+4] = b address (second operand)
;   [bp+3] = (return value slot - not used)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;
; Caller convention:
;   push result_addr
;   push a_addr
;   push b_addr
;   sub sp, 1
;   call _sub_bigfloat
;   add sp, 4
; ============================================================
_sub_bigfloat:
    push bp
    mov bp, sp

    ; Negate b's sign: b.sign = -b.sign
    mov ax, [bp+4]   ; b addr
    mov bx, [ax]     ; b.sign
    mov cx, 0
    sub cx, bx       ; -b.sign
    mov [ax], cx     ; b.sign = -b.sign

    ; Call add: result = a + (-b)
    mov ax, [bp+6]   ; result addr
    push ax
    mov ax, [bp+5]   ; a addr
    push ax
    mov ax, [bp+4]   ; b addr
    push ax
    sub sp, 1
    call _add_bigfloat
    add sp, 4

    ; Restore b's sign: b.sign = -b.sign
    mov ax, [bp+4]   ; b addr
    mov bx, [ax]     ; b.sign (currently negated)
    mov cx, 0
    sub cx, bx       ; restore original
    mov [ax], cx

    mov sp, bp
    pop bp
    ret

; ============================================================
; _mul_bigfloat: Multiply two BigFloat numbers
;
; result = a * b
;
; Algorithm:
;   1. temp[0..2*PRECISION-1] = 0
;   2. for i = 0 to PRECISION-1:
;        for j = 0 to PRECISION-1:
;          temp[i+j] += a.values[i] * b.values[j]
;   3. Normalize temp array (handle carries)
;   4. Copy temp[0..PRECISION-1] to result.values
;   5. result.sign = a.sign * b.sign
;   6. result.exponent = a.exponent + b.exponent
;   7. Normalize result
;
; Stack frame:
;   [bp+6] = result address
;   [bp+5] = a address
;   [bp+4] = b address
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: i
;   [bp-1] = local: j
;   [bp-2] = local: temp[0]
;   [bp-3] = local: temp[1]
;   ...
;   [bp-33] = local: temp[31]  (2*PRECISION-1 = 31)
;
; Caller convention:
;   push result_addr
;   push a_addr
;   push b_addr
;   sub sp, 1
;   call _mul_bigfloat
;   add sp, 4
; ============================================================
_mul_bigfloat:
    push bp
    mov bp, sp
    sub sp, 34       ; 2 locals (i, j) + 32 temp array

    ; --------------------------------------------------------
    ; Step 1: Initialize temp[0..27] to 0
    ; --------------------------------------------------------
    mov cx, 0        ; i = 0
_mul_init_temp:
    mov ax, 0
    mov ax, [ax+2]   ; PRECISION
    add ax, ax       ; 2 * PRECISION
    cmp cx, ax
    jge _mul_init_temp_done

    ; temp[i] = 0  (temp starts at bp-2, so temp[i] is at bp-2-i)
    mov ax, bp
    sub ax, 2
    sub ax, cx       ; &temp[i]
    mov bx, 0
    mov [ax], bx

    add cx, 1
    jmp _mul_init_temp

_mul_init_temp_done:
    ; --------------------------------------------------------
    ; Step 2: Nested multiplication loop
    ; for i = 0 to PRECISION-1:
    ;   for j = 0 to PRECISION-1:
    ;     temp[i+j] += a.values[i] * b.values[j]
    ; --------------------------------------------------------
    mov ax, 0
    mov [bp+0], ax   ; i = 0

_mul_outer_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _mul_carry_phase

    ; Inner loop: j = 0
    mov ax, 0
    mov [bp-1], ax   ; j = 0

_mul_inner_loop:
    mov ax, [bp-1]   ; j
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _mul_inner_done

    ; Compute a.values[i] * b.values[j]
    ; Load a.values[i]
    mov bx, [bp+5]   ; a addr
    add bx, 2        ; &a.values[0]
    add bx, [bp+0]   ; &a.values[i]
    mov cx, [bx]     ; a.values[i]

    ; Load b.values[j]
    mov bx, [bp+4]   ; b addr
    add bx, 2        ; &b.values[0]
    add bx, ax       ; &b.values[j]
    mov dx, [bx]     ; b.values[j]

    ; Multiply: ax = a.values[i] * b.values[j]
    mov ax, cx
    mul dx           ; ax = cx * dx

    ; Add to temp[i+j]
    ; temp index = i + j
    mov bx, [bp+0]   ; i
    add bx, [bp-1]   ; i + j

    ; temp[i+j] address = bp - 2 - (i+j)
    mov cx, bp
    sub cx, 2
    sub cx, bx       ; &temp[i+j]

    ; temp[i+j] += product
    mov dx, [cx]     ; current temp[i+j]
    add dx, ax       ; + product
    mov [cx], dx

    ; j++
    mov ax, [bp-1]
    add ax, 1
    mov [bp-1], ax
    jmp _mul_inner_loop

_mul_inner_done:
    ; i++
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _mul_outer_loop

_mul_carry_phase:
    ; --------------------------------------------------------
    ; Step 3: Normalize temp array (handle carries)
    ; for i = 2*PRECISION-1 down to 1
    ; --------------------------------------------------------
    mov ax, 0
    mov ax, [ax+2]   ; PRECISION
    add ax, ax       ; 2 * PRECISION
    sub ax, 1        ; i = 2*PRECISION - 1
    mov [bp+0], ax

_mul_carry_loop:
    mov ax, [bp+0]   ; i
    cmp ax, 1
    jl _mul_copy_result

    ; Load temp[i]
    mov bx, bp
    sub bx, 2
    sub bx, ax       ; &temp[i]
    mov cx, [bx]     ; temp[i]

    ; Check if temp[i] >= BASE
    mov dx, 0
    mov dx, [dx+1]   ; BASE
    cmp cx, dx
    jl _mul_carry_next

    ; carry = temp[i] / BASE
    ; temp[i] = temp[i] % BASE
    mov ax, cx       ; ax = temp[i]
    div dx           ; ax = quotient (carry), dx = remainder
    mov [bx], dx     ; temp[i] = remainder

    ; temp[i-1] += carry
    mov cx, [bp+0]   ; i
    sub cx, 1        ; i - 1
    mov dx, bp
    sub dx, 2
    sub dx, cx       ; &temp[i-1]
    mov cx, [dx]     ; temp[i-1]
    add cx, ax       ; + carry
    mov [dx], cx

_mul_carry_next:
    mov ax, [bp+0]
    sub ax, 1
    mov [bp+0], ax
    jmp _mul_carry_loop

_mul_copy_result:
    ; --------------------------------------------------------
    ; Step 4: Copy temp[0..PRECISION-1] to result.values
    ; --------------------------------------------------------
    mov ax, 0
    mov [bp+0], ax   ; i = 0

_mul_copy_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _mul_set_sign

    ; Load temp[i]
    mov bx, bp
    sub bx, 2
    sub bx, ax       ; &temp[i]
    mov cx, [bx]     ; temp[i]

    ; Store to result.values[i]
    mov bx, [bp+6]   ; result addr
    add bx, 2        ; &result.values[0]
    add bx, ax       ; &result.values[i]
    mov [bx], cx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _mul_copy_loop

_mul_set_sign:
    ; --------------------------------------------------------
    ; Step 5: result.sign = a.sign * b.sign
    ; --------------------------------------------------------
    mov ax, [bp+5]   ; a addr
    mov bx, [ax]     ; a.sign
    mov ax, [bp+4]   ; b addr
    mov cx, [ax]     ; b.sign
    mov ax, bx
    mul cx           ; ax = a.sign * b.sign
    mov bx, [bp+6]   ; result addr
    mov [bx], ax     ; result.sign

    ; --------------------------------------------------------
    ; Step 6: result.exponent = a.exponent + b.exponent
    ; --------------------------------------------------------
    mov ax, [bp+5]   ; a addr
    add ax, 1        ; &a.exponent
    mov bx, [ax]     ; a.exponent
    mov ax, [bp+4]   ; b addr
    add ax, 1        ; &b.exponent
    mov cx, [ax]     ; b.exponent
    add bx, cx       ; a.exp + b.exp
    mov ax, [bp+6]   ; result addr
    add ax, 1        ; &result.exponent
    mov [ax], bx

    ; --------------------------------------------------------
    ; Step 7: Normalize result
    ; --------------------------------------------------------
    mov ax, [bp+6]   ; result addr
    push ax
    sub sp, 1
    call _normalize
    add sp, 2

    mov sp, bp
    pop bp
    ret

; ============================================================
; _dump_bigfloat: Print internal details of a BigFloat
;
; Output format:
;   BigFloat@<addr>: sign=<sign> exp=<exp> values=[v0, v1, v2, ...]
;
; Stack frame:
;   [bp+4] = BigFloat address
;   [bp+3] = (return value slot - not used)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;
; Caller convention:
;   push addr
;   sub sp, 1
;   call _dump_bigfloat
;   add sp, 2
; ============================================================
_dump_bigfloat:
    push bp
    mov bp, sp
    sub sp, 1        ; 1 local variable

    ; Print header
    print "BigFloat@"
    print [bp+4]
    print ": sign="

    ; Print sign
    mov ax, [bp+4]
    print [ax+0]

    ; Print exponent
    print " exp="
    mov ax, [bp+4]
    add ax, 1
    print [ax]

    ; Print values array
    print " values=["

    ; Loop: for i = 0 to PRECISION-1
    mov cx, 0
    mov [bp+0], cx

_dump_values_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _dump_values_done

    ; Print comma separator (except for first element)
    cmp ax, 0
    je _dump_skip_comma
    print ", "

_dump_skip_comma:
    ; Print values[i]
    mov bx, [bp+4]   ; BigFloat addr
    add bx, 2        ; &values[0]
    add bx, ax       ; &values[i]
    print [bx]

    ; i++
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _dump_values_loop

_dump_values_done:
    println "]"

    mov sp, bp
    pop bp
    ret

; ============================================================
; _div_bigfloat: Divide two BigFloat numbers
;
; result = a / b
;
; Uses simplified long division with divisor's first element.
; This works well for dividing by integers or simple divisors.
;
; Algorithm:
;   1. Check for division by zero
;   2. result.sign = a.sign * b.sign
;   3. result.exponent = a.exponent - b.exponent
;   4. Long division:
;      remainder = 0
;      for i = 0 to PRECISION-1:
;        current = remainder * BASE + a.values[i]
;        result.values[i] = current / divisor
;        remainder = current % divisor
;   5. Normalize result
;
; Stack frame:
;   [bp+6] = result address
;   [bp+5] = a address (dividend)
;   [bp+4] = b address (divisor)
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;   [bp-1] = local: remainder
;   [bp-2] = local: divisor_val (b.values[0])
;
; Caller convention:
;   push result_addr
;   push a_addr
;   push b_addr
;   sub sp, 1
;   call _div_bigfloat
;   add sp, 4
; ============================================================
_div_bigfloat:
    push bp
    mov bp, sp
    sub sp, 3        ; 3 local variables

    ; --------------------------------------------------------
    ; Step 1: Get divisor value (b.values[0]) and check for zero
    ; --------------------------------------------------------
    mov ax, [bp+4]   ; b addr
    add ax, 2        ; &b.values[0]
    mov bx, [ax]     ; divisor_val = b.values[0]
    mov [bp-2], bx   ; save divisor_val

    ; Check for division by zero
    cmp bx, 0
    jne _div_not_zero

    ; Division by zero - print error and halt
    println "Error: Division by zero"
    halt

_div_not_zero:
    ; --------------------------------------------------------
    ; Step 2: result.sign = a.sign * b.sign
    ; --------------------------------------------------------
    mov ax, [bp+5]   ; a addr
    mov bx, [ax]     ; a.sign
    mov ax, [bp+4]   ; b addr
    mov cx, [ax]     ; b.sign
    mov ax, bx
    mul cx           ; ax = a.sign * b.sign
    mov bx, [bp+6]   ; result addr
    mov [bx], ax     ; result.sign

    ; --------------------------------------------------------
    ; Step 3: result.exponent = a.exponent - b.exponent
    ; --------------------------------------------------------
    mov ax, [bp+5]   ; a addr
    add ax, 1        ; &a.exponent
    mov bx, [ax]     ; a.exponent
    mov ax, [bp+4]   ; b addr
    add ax, 1        ; &b.exponent
    mov cx, [ax]     ; b.exponent
    sub bx, cx       ; a.exp - b.exp
    mov ax, [bp+6]   ; result addr
    add ax, 1        ; &result.exponent
    mov [ax], bx

    ; --------------------------------------------------------
    ; Step 4: Long division loop
    ; remainder = 0
    ; for i = 0 to PRECISION-1:
    ;   current = remainder * BASE + a.values[i]
    ;   result.values[i] = current / divisor
    ;   remainder = current % divisor
    ; --------------------------------------------------------
    mov ax, 0
    mov [bp-1], ax   ; remainder = 0
    mov [bp+0], ax   ; i = 0

_div_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _div_normalize

    ; current = remainder * BASE + a.values[i]
    ; First: remainder * BASE
    mov ax, [bp-1]   ; remainder
    mov dx, 0
    mov dx, [dx+1]   ; BASE
    mul dx           ; ax = remainder * BASE

    ; Then add a.values[i]
    mov bx, [bp+5]   ; a addr
    add bx, 2        ; &a.values[0]
    add bx, [bp+0]   ; &a.values[i]
    mov cx, [bx]     ; a.values[i]
    add ax, cx       ; current = remainder * BASE + a.values[i]

    ; Divide: quotient = current / divisor, remainder = current % divisor
    mov dx, [bp-2]   ; divisor_val
    div dx           ; ax = quotient, dx = remainder

    ; Store quotient in result.values[i]
    mov bx, [bp+6]   ; result addr
    add bx, 2        ; &result.values[0]
    add bx, [bp+0]   ; &result.values[i]
    mov [bx], ax     ; result.values[i] = quotient

    ; Update remainder
    mov [bp-1], dx   ; remainder = dx

    ; i++
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _div_loop

_div_normalize:
    ; --------------------------------------------------------
    ; Step 5: Normalize result
    ; --------------------------------------------------------
    mov ax, [bp+6]   ; result addr
    push ax
    sub sp, 1
    call _normalize
    add sp, 2

    mov sp, bp
    pop bp
    ret

; ============================================================
; _copy_bigfloat: Copy a BigFloat to another location
;
; dest = src (deep copy)
;
; Stack frame:
;   [bp+5] = dest address
;   [bp+4] = src address
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;
; Caller convention:
;   push dest_addr
;   push src_addr
;   sub sp, 1
;   call _copy_bigfloat
;   add sp, 3
; ============================================================
_copy_bigfloat:
    push bp
    mov bp, sp
    sub sp, 1        ; 1 local variable

    ; Copy sign
    mov ax, [bp+4]   ; src addr
    mov bx, [ax]     ; src.sign
    mov ax, [bp+5]   ; dest addr
    mov [ax], bx     ; dest.sign = src.sign

    ; Copy exponent
    mov ax, [bp+4]
    add ax, 1
    mov bx, [ax]     ; src.exponent
    mov ax, [bp+5]
    add ax, 1
    mov [ax], bx     ; dest.exponent = src.exponent

    ; Copy values array
    mov cx, 0
    mov [bp+0], cx   ; i = 0

_copy_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _copy_done

    ; dest.values[i] = src.values[i]
    mov bx, [bp+4]   ; src addr
    add bx, 2
    add bx, ax       ; &src.values[i]
    mov cx, [bx]     ; src.values[i]

    mov bx, [bp+5]   ; dest addr
    add bx, 2
    add bx, ax       ; &dest.values[i]
    mov [bx], cx     ; dest.values[i] = src.values[i]

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _copy_loop

_copy_done:
    mov sp, bp
    pop bp
    ret

; ============================================================
; _truncate_bigfloat: Truncate BigFloat to integer
;
; Removes fractional part, rounds toward zero.
; result = truncate(src)
;
; Stack frame:
;   [bp+5] = result address
;   [bp+4] = src address
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;   [bp-1] = local: int_elements (exponent + 1)
;
; Caller convention:
;   push result_addr
;   push src_addr
;   sub sp, 1
;   call _truncate_bigfloat
;   add sp, 3
; ============================================================
_truncate_bigfloat:
    push bp
    mov bp, sp
    sub sp, 2        ; 2 local variables

    ; First, copy src to result
    mov ax, [bp+5]   ; result addr
    push ax
    mov ax, [bp+4]   ; src addr
    push ax
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    ; Check if exponent < 0 (purely fractional)
    mov ax, [bp+5]   ; result addr
    add ax, 1
    mov bx, [ax]     ; exponent
    cmp bx, 0
    jge _trunc_not_fractional

    ; Purely fractional: set result to 0
    mov ax, [bp+5]   ; result addr
    mov bx, 1
    mov [ax], bx     ; sign = 1
    add ax, 1
    mov bx, 0
    mov [ax], bx     ; exponent = 0

    ; Set all values to 0
    mov cx, 0
    mov [bp+0], cx

_trunc_zero_loop:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _trunc_done

    mov bx, [bp+5]
    add bx, 2
    add bx, ax
    mov cx, 0
    mov [bx], cx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _trunc_zero_loop

_trunc_not_fractional:
    ; int_elements = exponent + 1
    mov ax, [bp+5]   ; result addr
    add ax, 1
    mov bx, [ax]     ; exponent
    add bx, 1        ; int_elements = exponent + 1
    mov [bp-1], bx

    ; Zero out values[int_elements] through values[PRECISION-1]
    mov ax, bx       ; i = int_elements
    mov [bp+0], ax

_trunc_zero_frac_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _trunc_normalize

    ; result.values[i] = 0
    mov bx, [bp+5]   ; result addr
    add bx, 2
    add bx, ax       ; &result.values[i]
    mov cx, 0
    mov [bx], cx

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _trunc_zero_frac_loop

_trunc_normalize:
    ; Normalize result
    mov ax, [bp+5]
    push ax
    sub sp, 1
    call _normalize
    add sp, 2

_trunc_done:
    mov sp, bp
    pop bp
    ret

; ============================================================
; _mod_bigfloat: Modulo operation
;
; result = a % b = a - truncate(a / b) * b
;
; Stack frame:
;   [bp+6] = result address
;   [bp+5] = a address
;   [bp+4] = b address
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: temp1 addr (for quotient)
;   [bp-1] = local: temp2 addr (for truncated quotient)
;   [bp-2] = local: temp3 addr (for quotient * b)
;
; Note: Uses addresses 540, 558, 576 as temp storage (aligned to 18)
;
; Caller convention:
;   push result_addr
;   push a_addr
;   push b_addr
;   sub sp, 1
;   call _mod_bigfloat
;   add sp, 4
; ============================================================
_mod_bigfloat:
    push bp
    mov bp, sp
    sub sp, 3        ; 3 local variables

    ; Use fixed temp addresses (must not conflict with test data)
    mov ax, 540
    mov [bp+0], ax   ; temp1 = 540 (quotient)
    mov ax, 558
    mov [bp-1], ax   ; temp2 = 558 (truncated quotient)
    mov ax, 576
    mov [bp-2], ax   ; temp3 = 576 (quotient * b)

    ; Step 1: temp1 = a / b
    mov ax, [bp+0]   ; temp1 addr
    push ax
    mov ax, [bp+5]   ; a addr
    push ax
    mov ax, [bp+4]   ; b addr
    push ax
    sub sp, 1
    call _div_bigfloat
    add sp, 4

    ; Step 2: temp2 = truncate(temp1)
    mov ax, [bp-1]   ; temp2 addr
    push ax
    mov ax, [bp+0]   ; temp1 addr
    push ax
    sub sp, 1
    call _truncate_bigfloat
    add sp, 3

    ; Step 3: temp3 = temp2 * b
    mov ax, [bp-2]   ; temp3 addr
    push ax
    mov ax, [bp-1]   ; temp2 addr
    push ax
    mov ax, [bp+4]   ; b addr
    push ax
    sub sp, 1
    call _mul_bigfloat
    add sp, 4

    ; Step 4: result = a - temp3
    mov ax, [bp+6]   ; result addr
    push ax
    mov ax, [bp+5]   ; a addr
    push ax
    mov ax, [bp-2]   ; temp3 addr
    push ax
    sub sp, 1
    call _sub_bigfloat
    add sp, 4

    mov sp, bp
    pop bp
    ret

; ============================================================
; _cmp_bigfloat: Compare two BigFloat numbers
;
; Returns: -1 if a < b, 0 if a == b, 1 if a > b
;
; Algorithm:
;   1. Check if both are zero -> return 0
;   2. Check if a is zero -> return based on b's sign
;   3. Check if b is zero -> return a's sign
;   4. Different signs -> return a's sign
;   5. Same sign: compare exponents
;   6. Same exponent: compare values element by element
;
; Stack frame:
;   [bp+5] = a address
;   [bp+4] = b address
;   [bp+3] = return value slot (will store -1, 0, or 1)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;   [bp-1] = local: a_is_zero flag
;   [bp-2] = local: b_is_zero flag
;
; Caller convention:
;   push a_addr
;   push b_addr
;   sub sp, 1
;   call _cmp_bigfloat
;   mov ax, [sp+1]   ; get result
;   add sp, 3
; ============================================================
_cmp_bigfloat:
    push bp
    mov bp, sp
    sub sp, 3        ; 3 local variables

    ; --------------------------------------------------------
    ; Check if a is zero (all values == 0)
    ; --------------------------------------------------------
    mov cx, 1        ; assume zero (flag = 1)
    mov ax, 0
    mov [bp+0], ax   ; i = 0

_cmp_check_a_zero:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _cmp_a_zero_done

    mov bx, [bp+5]   ; a addr
    add bx, 2
    add bx, ax       ; &a.values[i]
    mov dx, [bx]
    cmp dx, 0
    je _cmp_a_zero_next

    ; Found non-zero, a is not zero
    mov cx, 0
    jmp _cmp_a_zero_done

_cmp_a_zero_next:
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _cmp_check_a_zero

_cmp_a_zero_done:
    mov [bp-1], cx   ; a_is_zero flag

    ; --------------------------------------------------------
    ; Check if b is zero (all values == 0)
    ; --------------------------------------------------------
    mov cx, 1        ; assume zero
    mov ax, 0
    mov [bp+0], ax   ; i = 0

_cmp_check_b_zero:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _cmp_b_zero_done

    mov bx, [bp+4]   ; b addr
    add bx, 2
    add bx, ax       ; &b.values[i]
    mov dx, [bx]
    cmp dx, 0
    je _cmp_b_zero_next

    ; Found non-zero, b is not zero
    mov cx, 0
    jmp _cmp_b_zero_done

_cmp_b_zero_next:
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _cmp_check_b_zero

_cmp_b_zero_done:
    mov [bp-2], cx   ; b_is_zero flag

    ; --------------------------------------------------------
    ; Handle zero cases
    ; --------------------------------------------------------
    ; If both zero, return 0
    mov ax, [bp-1]   ; a_is_zero
    cmp ax, 0
    je _cmp_check_b_only_zero
    mov ax, [bp-2]   ; b_is_zero
    cmp ax, 0
    je _cmp_check_b_only_zero

    ; Both are zero
    mov ax, 0
    mov [bp+3], ax
    jmp _cmp_done

_cmp_check_b_only_zero:
    ; If a is zero (but not b)
    mov ax, [bp-1]
    cmp ax, 0
    je _cmp_check_a_only_zero

    ; a is zero, return based on b's sign
    ; if b.sign < 0, return 1; else return -1
    mov bx, [bp+4]   ; b addr
    mov ax, [bx]     ; b.sign
    cmp ax, 0
    jl _cmp_a_zero_b_neg

    ; b is positive, a(0) < b, return -1
    mov ax, -1
    mov [bp+3], ax
    jmp _cmp_done

_cmp_a_zero_b_neg:
    ; b is negative, a(0) > b, return 1
    mov ax, 1
    mov [bp+3], ax
    jmp _cmp_done

_cmp_check_a_only_zero:
    ; If b is zero (but not a)
    mov ax, [bp-2]
    cmp ax, 0
    je _cmp_check_signs

    ; b is zero, return a's sign
    mov bx, [bp+5]   ; a addr
    mov ax, [bx]     ; a.sign
    mov [bp+3], ax
    jmp _cmp_done

_cmp_check_signs:
    ; --------------------------------------------------------
    ; Neither is zero, check signs
    ; --------------------------------------------------------
    mov bx, [bp+5]   ; a addr
    mov ax, [bx]     ; a.sign
    mov bx, [bp+4]   ; b addr
    mov cx, [bx]     ; b.sign

    cmp ax, cx
    je _cmp_same_sign

    ; Different signs: return a.sign
    mov [bp+3], ax
    jmp _cmp_done

_cmp_same_sign:
    ; --------------------------------------------------------
    ; Same sign: compare exponents
    ; --------------------------------------------------------
    mov dx, ax       ; save sign_multiplier in dx

    mov bx, [bp+5]   ; a addr
    add bx, 1
    mov ax, [bx]     ; a.exponent

    mov bx, [bp+4]   ; b addr
    add bx, 1
    mov cx, [bx]     ; b.exponent

    cmp ax, cx
    je _cmp_same_exp

    ; Different exponents
    jg _cmp_a_exp_greater

    ; a.exp < b.exp: return -sign_multiplier
    mov ax, 0
    sub ax, dx
    mov [bp+3], ax
    jmp _cmp_done

_cmp_a_exp_greater:
    ; a.exp > b.exp: return sign_multiplier
    mov [bp+3], dx
    jmp _cmp_done

_cmp_same_exp:
    ; --------------------------------------------------------
    ; Same exponent: compare values element by element
    ; --------------------------------------------------------
    mov [bp-1], dx   ; save sign_multiplier

    mov ax, 0
    mov [bp+0], ax   ; i = 0

_cmp_values_loop:
    mov ax, [bp+0]   ; i
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _cmp_equal

    ; Compare a.values[i] with b.values[i]
    mov bx, [bp+5]   ; a addr
    add bx, 2
    add bx, ax       ; &a.values[i]
    mov cx, [bx]     ; a.values[i]

    mov bx, [bp+4]   ; b addr
    add bx, 2
    add bx, ax       ; &b.values[i]
    mov dx, [bx]     ; b.values[i]

    cmp cx, dx
    je _cmp_values_next

    ; Values differ
    jg _cmp_a_val_greater

    ; a.values[i] < b.values[i]: return -sign_multiplier
    mov ax, 0
    sub ax, [bp-1]
    mov [bp+3], ax
    jmp _cmp_done

_cmp_a_val_greater:
    ; a.values[i] > b.values[i]: return sign_multiplier
    mov ax, [bp-1]
    mov [bp+3], ax
    jmp _cmp_done

_cmp_values_next:
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _cmp_values_loop

_cmp_equal:
    ; All values equal, return 0
    mov ax, 0
    mov [bp+3], ax

_cmp_done:
    mov sp, bp
    pop bp
    ret

; ============================================================
; _print_padded: Print a number with leading zeros (7 digits)
;
; Prints value as 7-digit number with leading zeros
; e.g., 123 prints as "0000123"
;
; Stack frame:
;   [bp+4] = value to print
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: divisor
;
; Caller convention:
;   push value
;   sub sp, 1
;   call _print_padded
;   add sp, 2
; ============================================================
_print_padded:
    push bp
    mov bp, sp
    sub sp, 1

    mov ax, [bp+4]   ; value
    mov cx, 1000000  ; divisor = 10^6 (for 7 digits)
    mov [bp+0], cx

_print_padded_loop:
    mov cx, [bp+0]   ; divisor
    cmp cx, 0
    je _print_padded_done

    ; digit = value / divisor
    div cx           ; ax = digit, dx = remainder
    print ax         ; print the digit

    ; value = remainder
    mov ax, dx

    ; divisor = divisor / 10
    mov cx, [bp+0]
    push ax          ; save value
    mov ax, cx
    div 10
    mov [bp+0], ax   ; divisor /= 10
    pop ax           ; restore value

    jmp _print_padded_loop

_print_padded_done:
    mov sp, bp
    pop bp
    ret

; ============================================================
; _print_bigfloat: Print a BigFloat in decimal format
;
; Prints the number in human-readable decimal format.
; Simplified version that handles common cases.
;
; Stack frame:
;   [bp+4] = BigFloat address
;   [bp+3] = (return value slot)
;   [bp+2] = saved ip
;   [bp+1] = saved bp
;   [bp+0] = local: loop counter i
;   [bp-1] = local: int_elements (exponent + 1)
;   [bp-2] = local: found_nonzero flag
;
; Caller convention:
;   push addr
;   sub sp, 1
;   call _print_bigfloat
;   add sp, 2
; ============================================================
_print_bigfloat:
    push bp
    mov bp, sp
    sub sp, 3        ; 3 local variables

    ; Check if all values are zero
    mov cx, 0        ; found_nonzero = 0
    mov ax, 0
    mov [bp+0], ax   ; i = 0

_print_check_zero:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _print_check_zero_done

    mov bx, [bp+4]   ; BigFloat addr
    add bx, 2
    add bx, ax
    mov dx, [bx]     ; values[i]
    cmp dx, 0
    je _print_check_zero_next
    mov cx, 1        ; found nonzero

_print_check_zero_next:
    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _print_check_zero

_print_check_zero_done:
    mov [bp-2], cx   ; save found_nonzero flag
    cmp cx, 0
    jne _print_not_zero

    ; All zeros, print "0"
    print "0"
    jmp _print_done

_print_not_zero:
    ; Print sign if negative
    mov bx, [bp+4]   ; BigFloat addr
    mov ax, [bx]     ; sign
    cmp ax, 0
    jge _print_sign_done
    print "-"

_print_sign_done:
    ; Get exponent
    mov bx, [bp+4]
    add bx, 1
    mov ax, [bx]     ; exponent

    ; int_elements = exponent + 1
    add ax, 1
    mov [bp-1], ax

    ; Check if exponent < 0 (number < 1)
    mov bx, [bp+4]
    add bx, 1
    mov ax, [bx]     ; exponent
    cmp ax, 0
    jl _print_fractional

    ; --------------------------------------------------------
    ; exponent >= 0: Print integer part, then decimal, then fraction
    ; --------------------------------------------------------

    ; Print values[0] (no padding for first digit)
    mov bx, [bp+4]
    add bx, 2
    mov ax, [bx]     ; values[0]
    print ax

    ; Print values[1] to values[int_elements-1] with padding
    mov ax, 1
    mov [bp+0], ax   ; i = 1

_print_int_loop:
    mov ax, [bp+0]
    cmp ax, [bp-1]   ; i < int_elements?
    jge _print_decimal

    ; Print values[i] with 7-digit padding
    mov bx, [bp+4]
    add bx, 2
    add bx, ax
    mov cx, [bx]     ; values[i]
    push cx
    sub sp, 1
    call _print_padded
    add sp, 2

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _print_int_loop

_print_decimal:
    ; Print decimal point
    print "."

    ; Print fractional part: values[int_elements] onwards
    mov ax, [bp-1]   ; i = int_elements
    mov [bp+0], ax

_print_frac_loop:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _print_done

    ; Print values[i] with 7-digit padding
    mov bx, [bp+4]
    add bx, 2
    add bx, ax
    mov cx, [bx]     ; values[i]
    push cx
    sub sp, 1
    call _print_padded
    add sp, 2

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _print_frac_loop

_print_fractional:
    ; --------------------------------------------------------
    ; exponent < 0: Print "0." then zeros then values
    ; --------------------------------------------------------
    print "0."

    ; Print leading zeros for negative exponent
    ; Need to print (-exponent - 1) groups of 7 zeros
    mov bx, [bp+4]
    add bx, 1
    mov ax, [bx]     ; exponent (negative)
    mov cx, 0
    sub cx, ax       ; -exponent
    sub cx, 1        ; -exponent - 1
    mov [bp+0], cx   ; number of zero groups

_print_leading_zeros:
    mov ax, [bp+0]
    cmp ax, 0
    jle _print_frac_values

    print "0000000"

    mov ax, [bp+0]
    sub ax, 1
    mov [bp+0], ax
    jmp _print_leading_zeros

_print_frac_values:
    ; Print all values with 7-digit padding (all are fractional)
    mov ax, 0
    mov [bp+0], ax   ; i = 0

_print_frac_values_loop:
    mov ax, [bp+0]
    mov dx, 0
    mov dx, [dx+2]   ; PRECISION
    cmp ax, dx
    jge _print_done

    ; All fractional values need 7-digit padding
    mov bx, [bp+4]
    add bx, 2
    add bx, ax
    mov cx, [bx]     ; values[i]
    push cx
    sub sp, 1
    call _print_padded
    add sp, 2

    mov ax, [bp+0]
    add ax, 1
    mov [bp+0], ax
    jmp _print_frac_values_loop

_print_done:
    mov sp, bp
    pop bp
    ret

; ============================================================
; Main program (placeholder for testing)
; ============================================================
; ============================================================
; Memory layout for pi calculation (aligned to 18 cells):
;   18: i (loop counter, starts at 1)
;   36: epsilon (precision threshold, 10^-105)
;   54: x (current term)
;   72: pi (accumulated result)
;   90: const_one (1)
;   108: const_two (2)
;   126: const_three (3)
;   144: const_four (4)
;   162: const_ten (10)
;   180: temp1
;   198: temp2
;   216: temp3
;   234: temp4
;   252: iteration counter (single memory cell)
; ============================================================

main:
    ; Print BASE to verify startup
    mov bx, 0
    print "BASE = "
    println [bx+1]

    println "===== Calculating Pi ====="

    ; Initialize constants
    ; const_one = 1 at addr 90
    push 90
    push 1
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; const_two = 2 at addr 108
    push 108
    push 2
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; const_three = 3 at addr 126
    push 126
    push 3
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; const_four = 4 at addr 144
    push 144
    push 4
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; const_ten = 10 at addr 162
    push 162
    push 10
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; i = 1 at addr 18
    push 18
    push 90
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    ; epsilon = 1 at addr 36
    push 36
    push 90
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    ; Divide epsilon by 10, 105 times to get 10^-105
    println "Calculating epsilon = 10^-105..."
    mov cx, 252      ; cx = address of iteration counter
    mov ax, 0
    mov [cx], ax     ; j = 0

_epsilon_loop:
    mov cx, 252
    mov ax, [cx]
    cmp ax, 105
    jge _epsilon_done

    ; epsilon = epsilon / 10
    push 180         ; temp1 = result
    push 36          ; epsilon
    push 162         ; const_ten
    sub sp, 1
    call _div_bigfloat
    add sp, 4

    ; Copy result back to epsilon
    push 36
    push 180
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    mov cx, 252
    mov ax, [cx]
    add ax, 1
    mov [cx], ax
    jmp _epsilon_loop

_epsilon_done:
    print "epsilon = "
    push 36
    sub sp, 1
    call _print_bigfloat
    add sp, 2
    println ""

    ; x = 3 (which is r * 3 where r = 1)
    push 54
    push 126
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    ; pi = x = 3
    push 72
    push 54
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    println "Starting iteration..."
    mov cx, 252
    mov ax, 0
    mov [cx], ax     ; iteration counter = 0

    ; ========================================
    ; Main loop: while x > epsilon
    ; ========================================
_pi_loop:
    ; Compare x with epsilon
    push 54          ; x
    push 36          ; epsilon
    sub sp, 1
    call _cmp_bigfloat
    mov ax, [sp+1]
    add sp, 3

    ; If x <= epsilon (cmp <= 0), exit loop
    cmp ax, 1
    jne _pi_done

    ; ----------------------------------------
    ; x = x * i / ((i + 1) * 4)
    ; ----------------------------------------

    ; temp1 = x * i
    push 180         ; temp1
    push 54          ; x
    push 18          ; i
    sub sp, 1
    call _mul_bigfloat
    add sp, 4

    ; temp2 = i + 1
    push 198         ; temp2
    push 18          ; i
    push 90          ; const_one
    sub sp, 1
    call _add_bigfloat
    add sp, 4

    ; temp3 = temp2 * 4 = (i + 1) * 4
    push 216         ; temp3
    push 198         ; temp2
    push 144         ; const_four
    sub sp, 1
    call _mul_bigfloat
    add sp, 4

    ; x = temp1 / temp3 = (x * i) / ((i + 1) * 4)
    push 54          ; x (result)
    push 180         ; temp1
    push 216         ; temp3
    sub sp, 1
    call _div_bigfloat
    add sp, 4

    ; ----------------------------------------
    ; pi = pi + x / (i + 2)
    ; ----------------------------------------

    ; temp1 = i + 2
    push 180         ; temp1
    push 18          ; i
    push 108         ; const_two
    sub sp, 1
    call _add_bigfloat
    add sp, 4

    ; temp2 = x / (i + 2)
    push 198         ; temp2
    push 54          ; x
    push 180         ; temp1
    sub sp, 1
    call _div_bigfloat
    add sp, 4

    ; pi = pi + temp2
    push 216         ; temp3 (result)
    push 72          ; pi
    push 198         ; temp2
    sub sp, 1
    call _add_bigfloat
    add sp, 4

    ; Copy result back to pi
    push 72
    push 216
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    ; ----------------------------------------
    ; i = i + 2
    ; ----------------------------------------
    push 180         ; temp1
    push 18          ; i
    push 108         ; const_two
    sub sp, 1
    call _add_bigfloat
    add sp, 4

    ; Copy result back to i
    push 18
    push 180
    sub sp, 1
    call _copy_bigfloat
    add sp, 3

    ; ----------------------------------------
    ; Print progress every iteration
    ; ----------------------------------------
    mov cx, 252
    mov ax, [cx]
    add ax, 1
    mov [cx], ax     ; iteration++

    ; Print iteration number and pi
    print "Iteration "
    mov cx, 252
    print [cx]
    print ": pi = "
    push 72
    sub sp, 1
    call _print_bigfloat
    add sp, 2
    println ""

    jmp _pi_loop

_pi_done:
    println ""
    println "===== Final Result ====="
    print "pi = "
    push 72
    sub sp, 1
    call _print_bigfloat
    add sp, 2
    println ""

    print "Iterations: "
    mov cx, 252
    println [cx]

    halt
