import {Operation} from './Operation';

export enum MemType {
    Data = "Data",
    BP = "BP",
    IP = "IP",
}

export enum ExecStatus {
    Ready = "Ready",
    Running = "Running",
    Paused = "Paused",
    Halted = "Halted",
}

export class ComputerStatus {
    sourceCode = $state(`; Example program: find prime
_start:
_main:
    mov ax, -10
_main_loop1:
    push ax
    call _f_is_prime
    mov bx, ax
    pop ax
    cmp bx, 1
    jne _next
    print ax
    print " "
_next:
    add ax, 1
    cmp ax, 1000
    je _finish
    jmp _main_loop1
_finish:
    println
    print "bye!"
    println
    halt

_f_is_prime:
    push bp
    mov bp, sp

    ; check if ax is prime
    mov ax, [bp+3]

    ; check <2, ==2
    cmp ax, 2
    jl _not_prime
    je _is_prime
    div 2
    cmp dx, 0
    je _not_prime

    ; check 3 to ax-1
    mov cx, 3
_f_is_prime_loop1:
    mov ax, [bp+3]
    cmp cx, ax
    jge _is_prime
    div cx
    cmp dx, 0
    je _not_prime
    add cx, 1
    jmp _f_is_prime_loop1
_not_prime:
    pop bp
    mov ax, 0
    ret
_is_prime:
    pop bp
    mov ax, 1
    ret
`);

    // Compiled operations and labels from backend
    operations = $state<Operation[]>([]);
    labels = $state<{ [key: string]: number }>({});

    // Memory (1024 cells)
    memory = $state<number[]>(new Array(1024));
    // Track special memory types (BP and IP) for debugging
    memoryTypes = $state<{ [addr: number]: MemType }>({});

    registers = $state({
        ax: 0,
        bx: 0,
        cx: 0,
        dx: 0,
        flg: 0,
        sp: 1023,
        bp: 1023,
        ip: 0,
    });

    execStatus = $state<ExecStatus>(ExecStatus.Ready);
    output = $state('');

    /**
     * Load compiled operations from backend response
     */
    loadCompiledCode(operations: any[], labels: { [key: string]: number }) {
        // Convert plain objects to Operation instances
        this.operations = operations.map(op => new Operation(op));
        this.labels = labels;
        this.reset();
    }

    /**
     * Reset computer state
     */
    reset() {
        // reset memory and register with special magic value
        this.memory.fill(-999);
        this.memoryTypes = {};
        this.registers = {
            ax: -999,
            bx: -999,
            cx: -999,
            dx: -999,
            flg: 0,
            sp: 1023,
            bp: 1023,
            ip: 0,
        };

        this.execStatus = ExecStatus.Ready;
        this.output = '';
    }

    /**
     * Get memory value at address
     */
    getMemValue(addr: number): number {
        if (addr < 0 || addr >= this.memory.length) {
            throw new Error(`Memory address out of bounds: ${addr}`);
        }
        return this.memory[addr];
    }

    /**
     * Set memory value at address
     */
    setMemValue(addr: number, value: number, type: MemType = MemType.Data) {
        if (addr < 0 || addr >= this.memory.length) {
            throw new Error(`Memory address out of bounds: ${addr}`);
        }
        this.memory[addr] = value;

        if (type !== MemType.Data) {
            this.memoryTypes[addr] = type;
        } else {
            delete this.memoryTypes[addr];
        }
    }

    /**
     * Get memory type at address
     */
    getMemType(addr: number): MemType {
        return this.memoryTypes[addr] || MemType.Data;
    }

    /**
     * Push value onto stack
     */
    pushStack(value: number, type: MemType = MemType.Data) {
        if (this.registers.sp < 0) {
            throw new Error('Stack overflow');
        }
        this.setMemValue(this.registers.sp, value, type);
        this.registers.sp--;
    }

    /**
     * Pop value from stack
     */
    popStack(): number {
        if (this.registers.sp >= 1023) {
            throw new Error('Stack underflow');
        }
        this.registers.sp++;
        return this.memory[this.registers.sp];
    }
}