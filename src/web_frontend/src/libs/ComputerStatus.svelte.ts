import {Operation} from './Operation';
import type {Operand} from "./Operand.ts";

export const MEMORY_SIZE = 1024;

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

    // Compiled operations
    operations = $state<Operation[]>([]);

    memory = $state<number[]>(this.initRandomMemory());
    memoryTypes = $state<{ [addr: number]: MemType }>({});
    registers = $state(this.initRandomRegisters());

    execStatus = $state<ExecStatus>(ExecStatus.Ready);
    output = $state('');

    // For input operation - stores the target operand when waiting for input
    inputTarget = $state<Operand | null>(null);
    // Store the execution state before waiting for input (to resume properly)
    previousExecStatus = $state<ExecStatus | null>(null);


    /**
     * Load compiled operations
     */
    loadCompiledCode(operations: Operation[]) {
        this.operations = operations;
        this.reset();
    }

    initRandVal() {
        return Math.floor(Math.random() * 20000 - 10000);
    }

    initRandomMemory() {
        let mem = new Array(MEMORY_SIZE);
        for (let i = 0; i < mem.length; i++) {
            mem[i] = this.initRandVal();
        }
        return mem;
    }

    initRandomRegisters() {
        return {
            ax: this.initRandVal(),
            bx: this.initRandVal(),
            cx: this.initRandVal(),
            dx: this.initRandVal(),
            flg: Math.floor(Math.random() * 3 - 1),
            sp: MEMORY_SIZE - 1,
            bp: MEMORY_SIZE - 1,
            ip: 0,
        };
    }

    /**
     * Reset computer state
     */
    reset() {
        this.memory = this.initRandomMemory();
        this.memoryTypes = {};
        this.registers = this.initRandomRegisters();
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
            throw new Error('栈顶部越界');
        }
        this.setMemValue(this.registers.sp, value, type);
        this.registers.sp--;
    }

    /**
     * Pop value from stack
     */
    popStack(): number {
        if (this.registers.sp >= MEMORY_SIZE - 1) {
            throw new Error('栈底部越界');
        }
        this.registers.sp++;
        delete this.memoryTypes[this.registers.sp];
        return this.memory[this.registers.sp];
    }
}