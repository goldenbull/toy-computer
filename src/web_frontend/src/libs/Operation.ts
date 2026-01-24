import {Operand} from './Operand';

export class Operation {
    // Pre-computed strings for rendering performance
    displayStr: string;
    offsetStr: string = '';

    constructor(
        public addr: number,
        public type: string,
        public labels: string[] = [],
        public p1: Operand | null = null,
        public p2: Operand | null = null,
        public action: string | null = null,
        public target: string | null = null,
    ) {
        this.displayStr = this.buildDisplayStr();
    }

    // Called by Compiler after resolving label references
    resolveTarget(targetAddr: number) {
        this.targetAddr = targetAddr;
        this.targetOffset = targetAddr - this.addr;
        this.offsetStr = this.targetOffset.toLocaleString("en", { signDisplay: 'always', useGrouping: false });
    }

    targetAddr: number | null = null;
    targetOffset: number | null = null;

    private buildDisplayStr(): string {
        const parts: string[] = [];
        parts.push(this.action ?? this.type);

        if (this.p1 !== null) {
            if (this.p2 !== null) {
                parts.push(this.p1.toString() + ",");
                parts.push(this.p2.toString());
            } else {
                parts.push(this.p1.toString());
            }
        }

        if (this.target !== null) {
            parts.push(this.target);
        }

        return parts.join(' ');
    }

}
