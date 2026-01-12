import {Operation} from './Operation';
import type {Operand} from "./Operand.ts";

export enum MemType {
    Data = "Data",
    BP = "BP",
    IP = "IP",
}

export enum ExecStatus {
    Ready = "Ready",
    Running = "Running",
    RunningAnimation = "RunningAnimation",
    Paused = "Paused",
    Halted = "Halted",
    WaitingForInput = "WaitingForInput",
}

export class ComputerStatus {
    sourceCode = $state(`; 请开始你的表演 :)\n`);

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

    // For input operation - stores the target operand when waiting for input
    inputTarget = $state<Operand | null>(null);
    // Store the execution state before waiting for input (to resume properly)
    previousExecStatus = $state<ExecStatus | null>(null);

    /**
     * Load compiled operations from backend response
     */
    loadCompiledCode(operations: any[], labels: { [key: string]: number }) {
        // Convert plain objects to Operation instances
        this.operations = operations.map(op => new Operation(op));
        this.labels = labels;
        this.reset();
    }

    initRandVal() {
        return Math.floor(Math.random() * 20000 - 10000);
    }

    /**
     * Reset computer state
     */
    reset() {
        // reset memory and register with random values
        // this.memory.fill(-999);
        // this.memoryTypes = {};
        // this.registers = {
        //     ax: -999,
        //     bx: -999,
        //     cx: -999,
        //     dx: -999,
        //     flg: 0,
        //     sp: 1023,
        //     bp: 1023,
        //     ip: 0,
        // };
        for (let i = 0; i < this.memory.length; i++) {
            this.memory[i] = this.initRandVal();
        }
        this.memoryTypes = {};
        this.registers = {
            ax: this.initRandVal(),
            bx: this.initRandVal(),
            cx: this.initRandVal(),
            dx: this.initRandVal(),
            flg: Math.floor(Math.random() * 3 - 1),
            sp: 1023,
            bp: 1023,
            ip: 0,
        };

        this.execStatus = ExecStatus.Ready;
        this.output = '';
    }

    /**
     * Set memory value at address
     */
    setMemValue(addr: number, value: number, type: MemType = MemType.Data) {
        if (addr < 0 || addr >= this.memory.length) {
            throw new Error(`内存越界: ${addr}`);
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
        delete this.memoryTypes[this.registers.sp];
        return this.memory[this.registers.sp];
    }
}