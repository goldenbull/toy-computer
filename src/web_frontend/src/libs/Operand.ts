export enum OperandType {
    Reg = "Reg",
    Mem = "Mem",
    Imm = "Imm",
    Str = "Str"
}

export class Operand {
    constructor(
        public tp: OperandType,
        public reg: string = "",
        public offset: number = 0,
        public immVal: number = 0,
        public text: string[] = [],
    ) {}

    /**
     * Get the memory address for a memory operand
     */
    memAddr(registers: { [key: string]: number }): number {
        if (this.tp !== OperandType.Mem) {
            throw new Error("Operand type must be Mem");
        }
        const regValue = registers[this.reg];
        return regValue + this.offset;
    }

    /**
     * Get the value of this operand
     */
    value(registers: { [key: string]: number }, memory: number[]): number | string {
        switch (this.tp) {
            case OperandType.Reg:
                return registers[this.reg];
            case OperandType.Mem:
                const addr = this.memAddr(registers);
                if (addr < 0 || addr >= memory.length) {
                    throw new Error(`内存越界: ${addr}`);
                }
                return memory[addr];
            case OperandType.Imm:
                return this.immVal;
            case OperandType.Str:
                return this.text[1];
            default:
                throw new Error(`Invalid Operand type: ${this.tp}`);
        }
    }

    toString(): string {
        switch (this.tp) {
            case OperandType.Reg:
                return this.reg;
            case OperandType.Mem:
                if (this.offset === 0) {
                    return `[${this.reg}]`;
                } else {
                    return `[${this.reg}${this.offset >= 0 ? '+' : ''}${this.offset}]`;
                }
            case OperandType.Imm:
                return String(this.immVal);
            case OperandType.Str:
                return this.text[0];
            default:
                throw new Error(`Invalid Operand type: ${this.tp}`);
        }
    }
}
