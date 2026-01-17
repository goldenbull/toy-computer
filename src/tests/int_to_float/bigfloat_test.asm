    ; ========== Test init function ==========
    println "--- Testing init ---"

    ; Test 1: BigFloat(42) at address 16
    print "BigFloat(42): "
    push 16
    push 42
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 16
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 2: BigFloat(-99) at address 32
    print "BigFloat(-99): "
    push 32
    push -99
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 32
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 3: BigFloat(20000000) at address 48 - exceeds BASE
    print "BigFloat(20000000): "
    push 48
    push 20000000
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 48
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 4: BigFloat(123456789) at address 64
    print "BigFloat(123456789): "
    push 64
    push 123456789
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 64
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; ========== Test add function ==========
    println "--- Testing add ---"

    ; Create BigFloat(58) at 80
    push 80
    push 58
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 5: 42 + 58 = 100
    print "42 + 58: "
    push 96
    push 16
    push 80
    sub sp, 1
    call _add_bigfloat
    add sp, 4
    push 96
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(100) at 112, BigFloat(9999900) at 128
    push 112
    push 100
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 128
    push 9999900
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 6: 100 + 9999900 = 10000000
    print "100 + 9999900: "
    push 144
    push 112
    push 128
    sub sp, 1
    call _add_bigfloat
    add sp, 4
    push 144
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(-99) at 160
    push 160
    push -99
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 7: 100 + (-99) = 1
    print "100 + (-99): "
    push 176
    push 112
    push 160
    sub sp, 1
    call _add_bigfloat
    add sp, 4
    push 176
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 8: 20000000 + 42
    print "20000000 + 42: "
    push 192
    push 48
    push 16
    sub sp, 1
    call _add_bigfloat
    add sp, 4
    push 192
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; ========== Test subtract function ==========
    println "--- Testing subtract ---"

    ; Test 9: 100 - 58 = 42
    print "100 - 58: "
    push 208
    push 112
    push 80
    sub sp, 1
    call _sub_bigfloat
    add sp, 4
    push 208
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 10: 42 - 100 = -58
    print "42 - 100: "
    push 224
    push 16
    push 112
    sub sp, 1
    call _sub_bigfloat
    add sp, 4
    push 224
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 11: 20000000 - 42
    print "20000000 - 42: "
    push 240
    push 48
    push 16
    sub sp, 1
    call _sub_bigfloat
    add sp, 4
    push 240
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Verify 42 unchanged after subtract
    print "42 after sub (unchanged): "
    push 16
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; ========== Test multiply function ==========
    println "--- Testing multiply ---"

    ; Create BigFloat(6) at 256, BigFloat(7) at 272
    push 256
    push 6
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 272
    push 7
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 12: 6 * 7 = 42
    print "6 * 7: "
    push 288
    push 256
    push 272
    sub sp, 1
    call _mul_bigfloat
    add sp, 4
    push 288
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(1000) at 304
    push 304
    push 1000
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 13: 1000 * 1000 = 1000000
    print "1000 * 1000: "
    push 320
    push 304
    push 304
    sub sp, 1
    call _mul_bigfloat
    add sp, 4
    push 320
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(5000) at 336, BigFloat(3000) at 352
    push 336
    push 5000
    sub sp, 1
    call _init_bigfloat
    add sp, 3
    push 352
    push 3000
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 14: 5000 * 3000 = 15000000
    print "5000 * 3000: "
    push 368
    push 336
    push 352
    sub sp, 1
    call _mul_bigfloat
    add sp, 4
    push 368
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(-6) at 384
    push 384
    push -6
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 15: -6 * 7 = -42
    print "-6 * 7: "
    push 400
    push 384
    push 272
    sub sp, 1
    call _mul_bigfloat
    add sp, 4
    push 400
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(-7) at 416
    push 416
    push -7
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 16: -6 * -7 = 42
    print "-6 * -7: "
    push 432
    push 384
    push 416
    sub sp, 1
    call _mul_bigfloat
    add sp, 4
    push 432
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; ========== Test divide function ==========
    println "--- Testing divide ---"

    ; Create BigFloat(2) at 448
    push 448
    push 2
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 17: 42 / 2 = 21
    print "42 / 2: "
    push 464
    push 16          ; 42 at addr 16
    push 448         ; 2 at addr 448
    sub sp, 1
    call _div_bigfloat
    add sp, 4
    push 464
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 18: 100 / 7 (non-exact division)
    ; 100/7 = 14.285714...
    print "100 / 7: "
    push 480
    push 112         ; 100 at addr 112
    push 272         ; 7 at addr 272
    sub sp, 1
    call _div_bigfloat
    add sp, 4
    push 480
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(1000000) at 496
    push 496
    push 1000000
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 19: 1000000 / 1000 = 1000
    print "1000000 / 1000: "
    push 512
    push 496         ; 1000000
    push 304         ; 1000 at addr 304
    sub sp, 1
    call _div_bigfloat
    add sp, 4
    push 512
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 20: 20000000 / 2 = 10000000 (should normalize)
    print "20000000 / 2: "
    push 528
    push 48          ; 20000000 at addr 48
    push 448         ; 2
    sub sp, 1
    call _div_bigfloat
    add sp, 4
    push 528
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 21: -42 / 7 = -6 (negative dividend)
    ; Use -99 at 32, divided by something... let's create -42 first
    push 544
    push -42
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    print "-42 / 7: "
    push 560
    push 544         ; -42
    push 272         ; 7
    sub sp, 1
    call _div_bigfloat
    add sp, 4
    push 560
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 22: 42 / -7 = -6 (negative divisor)
    print "42 / -7: "
    push 576
    push 16          ; 42
    push 416         ; -7 at addr 416
    sub sp, 1
    call _div_bigfloat
    add sp, 4
    push 576
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; ========== Test modulo function ==========
    println "--- Testing modulo ---"

    ; Create BigFloat(10) at 640
    push 640
    push 10
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Create BigFloat(3) at 656
    push 656
    push 3
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 23: 10 % 3 = 1
    print "10 % 3: "
    push 672
    push 640         ; 10
    push 656         ; 3
    sub sp, 1
    call _mod_bigfloat
    add sp, 4
    push 672
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 24: 100 % 7 = 2
    print "100 % 7: "
    push 688
    push 112         ; 100 at addr 112
    push 272         ; 7 at addr 272
    sub sp, 1
    call _mod_bigfloat
    add sp, 4
    push 688
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Create BigFloat(17) at 704
    push 704
    push 17
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Create BigFloat(5) at 720
    push 720
    push 5
    sub sp, 1
    call _init_bigfloat
    add sp, 3

    ; Test 25: 17 % 5 = 2
    print "17 % 5: "
    push 736
    push 704         ; 17
    push 720         ; 5
    sub sp, 1
    call _mod_bigfloat
    add sp, 4
    push 736
    sub sp, 1
    call _dump_bigfloat
    add sp, 2

    ; Test 26: 42 % 6 = 0 (exact division)
    print "42 % 6: "
    push 752
    push 16          ; 42 at addr 16
    push 256         ; 6 at addr 256
    sub sp, 1
    call _mod_bigfloat
    add sp, 4
    push 752
    sub sp, 1
    call _dump_bigfloat
    add sp, 2
