import {ComputerStatus, ExecStatus, MemType} from './ComputerStatus.svelte';
import {Operation} from './Operation';
import {Operand, OperandType} from './Operand';

/**
 * WebExecutor - executes operations on the ComputerStatus
 */
export class WebExecutor {
    private status: ComputerStatus;
    private onOutputChange?: () => void;

    constructor(status: ComputerStatus, onOutputChange?: () => void) {
        this.status = status;
        this.onOutputChange = onOutputChange;
    }

    /**
     * Execute an operation
     */
    private executeOperation(op: Operation) {
        switch (op.type) {
            case 'move':
                this.execMove(op);
                break;
            case 'add':
                this.execAdd(op);
                break;
            case 'sub':
                this.execSub(op);
                break;
            case 'mul':
                this.execMul(op);
                break;
            case 'div':
                this.execDiv(op);
                break;
            case 'cmp':
                this.execCmp(op);
                break;
            case 'jump':
                this.execJump(op);
                break;
            case 'call':
                this.execCall(op);
                break;
            case 'ret':
                this.execRet(op);
                break;
            case 'push':
                this.execPush(op);
                break;
            case 'pop':
                this.execPop(op);
                break;
            case 'input':
                this.execInput(op);
                break;
            case 'print':
                this.execPrint(op);
                break;
            case 'rand':
                this.execRand(op);
                break;
            case 'dump':
                this.execDump(op);
                break;
            case 'pause':
                this.execPause(op);
                break;
            case 'halt':
                this.execHalt(op);
                break;
            case 'nop':
                this.execNop(op);
                break;
            default:
                throw new Error(`Unknown operation type: ${op.type}`);
        }
    }

    /**
     * Get operand value
     */
    private getOperandValue(operand: Operand): number | string {
        return operand.value(this.status.registers, this.status.memory);
    }

    /**
     * Set operand value
     */
    private setOperandValue(operand: Operand, value: number) {
        if (operand.tp === OperandType.Reg) {
            this.status.registers[operand.reg as keyof typeof this.status.registers] = value;
        } else {
            const addr = operand.memAddr(this.status.registers);
            this.status.setMemValue(addr, value);
        }
    }

    // Operation implementations

    private execMove(op: Operation) {
        const value = this.getOperandValue(op.p2!) as number;
        this.setOperandValue(op.p1!, value);
        this.status.registers.ip++;
    }

    private execAdd(op: Operation) {
        const v1 = this.status.registers[op.p1!.reg as keyof typeof this.status.registers];
        const v2 = this.getOperandValue(op.p2!) as number;
        this.status.registers[op.p1!.reg as keyof typeof this.status.registers] = v1 + v2;
        this.status.registers.ip++;
    }

    private execSub(op: Operation) {
        const v1 = this.status.registers[op.p1!.reg as keyof typeof this.status.registers];
        const v2 = this.getOperandValue(op.p2!) as number;
        this.status.registers[op.p1!.reg as keyof typeof this.status.registers] = v1 - v2;
        this.status.registers.ip++;
    }

    private execMul(op: Operation) {
        const v1 = this.status.registers.ax;
        const v2 = this.getOperandValue(op.p1!) as number;
        this.status.registers.ax = v1 * v2;
        this.status.registers.ip++;
    }

    private execDiv(op: Operation) {
        const v1 = this.status.registers.ax;
        const v2 = this.getOperandValue(op.p1!) as number;

        if (v2 === 0) throw new Error('Divide by zero');

        // Truncate toward zero (C-style division)
        const quotient = Math.trunc(v1 / v2);
        const remainder = v1 - v2 * quotient;

        this.status.registers.ax = quotient;
        this.status.registers.dx = remainder;
        this.status.registers.ip++;
    }

    private execCmp(op: Operation) {
        const v1 = this.status.registers[op.p1!.reg as keyof typeof this.status.registers];
        const v2 = this.getOperandValue(op.p2!) as number;

        if (v1 > v2) {
            this.status.registers.flg = 1;
        } else if (v1 === v2) {
            this.status.registers.flg = 0;
        } else {
            this.status.registers.flg = -1;
        }
        this.status.registers.ip++;
    }

    private execJump(op: Operation) {
        const targetAddr = this.status.labels[op.target!];
        if (targetAddr === undefined) throw new Error(`Unknown label: ${op.target}`);

        const flg = this.status.registers.flg;
        let shouldJump = false;

        switch (op.action) {
            case 'jmp':
                shouldJump = true;
                break;
            case 'je':
                shouldJump = (flg === 0);
                break;
            case 'jne':
                shouldJump = (flg !== 0);
                break;
            case 'jg':
                shouldJump = (flg > 0);
                break;
            case 'jge':
                shouldJump = (flg >= 0);
                break;
            case 'jl':
                shouldJump = (flg < 0);
                break;
            case 'jle':
                shouldJump = (flg <= 0);
                break;
        }

        if (shouldJump) {
            this.status.registers.ip = targetAddr;
        } else {
            this.status.registers.ip++;
        }
    }

    private execCall(op: Operation) {
        const targetAddr = this.status.labels[op.target!];
        if (targetAddr === undefined) throw new Error(`Unknown label: ${op.target}`);

        // Push return address
        this.status.pushStack(this.status.registers.ip + 1, MemType.IP);
        this.status.registers.ip = targetAddr;
    }

    private execRet(op: Operation) {
        this.status.registers.ip = this.status.popStack();
    }

    private execPush(op: Operation) {
        if (op.action === 'push') {
            const value = this.getOperandValue(op.p1!) as number;

            // Special type for bp register
            const memType = (op.p1!.tp === OperandType.Reg && op.p1!.reg === 'bp')
                ? MemType.BP
                : MemType.Data;

            this.status.pushStack(value, memType);
        } else if (op.action === 'pushf') {
            this.status.pushStack(this.status.registers.flg);
        }

        this.status.registers.ip++;
    }

    private execPop(op: Operation) {
        const value = this.status.popStack();

        if (op.action === 'pop' && op.p1) {
            this.setOperandValue(op.p1, value);
        } else if (op.action === 'popf') {
            this.status.registers.flg = value;
        }

        this.status.registers.ip++;
    }

    private execInput(op: Operation) {
        // Store the current execution status before waiting for input
        this.status.previousExecStatus = this.status.execStatus;
        // Mark status as waiting for input and store the target operand
        this.status.execStatus = ExecStatus.WaitingForInput;
        this.status.inputTarget = op.p1!;
        // Don't increment IP - will be incremented when input is provided
    }

    private execPrint(op: Operation) {
        let text = '';
        if (op.p1) {
            const value = this.getOperandValue(op.p1);
            text = String(value);
        }

        if (op.action === 'println') {
            text += "\n";
        }

        this.appendOutput(text);

        this.status.registers.ip++;
    }

    private execRand(op: Operation) {
        const value = Math.floor(Math.random() * 1000);
        this.setOperandValue(op.p1!, value);

        this.status.registers.ip++;
    }

    private execDump(op: Operation) {
        // Dump is a no-op in web executor - the UI already shows all state
        this.status.registers.ip++;
    }

    private execPause(op: Operation) {
        // Pause switches to paused state
        this.status.execStatus = ExecStatus.Paused;
        this.status.registers.ip++;
    }

    private execHalt(op: Operation) {
        this.status.execStatus = ExecStatus.Halted;
        // Don't increment IP on halt
    }

    private execNop(op: Operation) {
        this.status.registers.ip++;
    }

    /**
     * Append text to output
     */
    private appendOutput(text: string) {
        this.status.output += text;
        if (this.onOutputChange) {
            this.onOutputChange();
        }
    }

    /**
     * Execute one instruction step
     */
    runOneStep(): boolean {
        if (this.status.execStatus === ExecStatus.Halted) {
            return false;
        }

        const ip = this.status.registers.ip;

        // Check if IP is out of bounds
        if (ip < 0 || ip >= this.status.operations.length) {
            this.status.execStatus = ExecStatus.Halted;
            // check if all operations executed, gracefully stop
            if (ip !== this.status.operations.length) {
                this.appendOutput(`\nError: IP out of bounds (${ip})\n`);
            }
            return false;
        }

        const operation = this.status.operations[ip];

        try {
            this.executeOperation(operation);
            return true;
        } catch (e) {
            this.status.execStatus = ExecStatus.Halted;
            this.appendOutput(`\nError: ${e}\n`);
            return false;
        }
    }

    /**
     * Run continuously until halt/pause/error
     * Executes in batches for performance, yielding periodically for UI updates
     */
    async runContinuous() {
        this.status.execStatus = ExecStatus.Running;

        const batchSize = 1000; // Execute 1000 instructions before yielding
        let stepCount = 0;

        while (this.status.execStatus === ExecStatus.Running) {
            const canContinue = this.runOneStep();

            if (!canContinue) {
                break;
            }

            stepCount++;

            // Yield every batchSize steps to allow UI updates and check for break
            if (stepCount >= batchSize) {
                await new Promise(resolve => setTimeout(resolve, 0));
                stepCount = 0;
            }
        }
    }

    /**
     * Run with animation - executes one step at a time with delays for visualization
     * Each instruction execution is visible to the user
     */
    async runAnimation(delayMs: number = 100) {
        this.status.execStatus = ExecStatus.RunningAnimation;

        while (this.status.execStatus === ExecStatus.RunningAnimation) {
            const canContinue = this.runOneStep();

            if (!canContinue) {
                break;
            }

            // Yield after each step to allow UI updates
            await new Promise(resolve => setTimeout(resolve, delayMs));
        }
    }

    /**
     * Stop continuous execution
     */
    breakExecution() {
        if (this.status.execStatus === ExecStatus.Running || this.status.execStatus === ExecStatus.RunningAnimation) {
            this.status.execStatus = ExecStatus.Paused;
        }
    }

    /**
     * Provide input value and continue execution
     */
    provideInput(value: string) {
        if (this.status.execStatus !== ExecStatus.WaitingForInput) {
            throw new Error('Not waiting for input');
        }

        if (!this.status.inputTarget) {
            throw new Error('No input target specified');
        }

        // Parse and validate input - strict integer check
        const trimmedValue = value.trim();

        // Check if the string is a valid integer format (optional +/- followed by digits)
        if (!/^[+-]?\d+$/.test(trimmedValue)) {
            throw new Error('输入错误，必须输入一个整数');
        }

        const numValue = parseInt(trimmedValue, 10);
        if (isNaN(numValue)) {
            throw new Error('输入错误，必须输入一个整数');
        }

        // Store the input value temporarily
        const inputTarget = this.status.inputTarget;
        const previousStatus = this.status.previousExecStatus;

        // Clear input state and close dialog first
        this.status.inputTarget = null;
        this.status.previousExecStatus = null;

        // Set status to indicate we're processing
        if (previousStatus === ExecStatus.Running) {
            this.status.execStatus = ExecStatus.Running;
        } else if (previousStatus === ExecStatus.RunningAnimation) {
            this.status.execStatus = ExecStatus.RunningAnimation;
        } else {
            this.status.execStatus = ExecStatus.Paused;
        }

        // Now try to set the value - this may throw an error for invalid memory address
        try {
            this.setOperandValue(inputTarget, numValue);
            this.status.registers.ip++;

            // corner case: this is the last operation
            if (this.status.registers.ip === this.status.operations.length) {
                this.status.execStatus = ExecStatus.Halted;
            }
        } catch (e) {
            // Memory address error or other execution error - halt execution
            this.status.execStatus = ExecStatus.Halted;
            this.appendOutput(`\n${e}\n`);
            throw e;
        }
    }
}
