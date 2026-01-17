import {Operand} from './Operand';

export class Operation {
    addr: number;
    type: string;
    labels: string[];
    p1: Operand | null;
    p2: Operand | null;
    action: string | null;
    target: string | null;
    targetAddr: number | null; // for jump and call
    cnt: number | null;

    constructor(data: any) {
        this.addr = data.addr;
        this.type = data.type;
        this.labels = data.labels || [];
        this.p1 = data.p1 ? new Operand(data.p1) : null;
        this.p2 = data.p2 ? new Operand(data.p2) : null;
        this.action = data.action || null;
        this.target = data.target || null;
        this.targetAddr = data.targetAddr || null;
        this.cnt = data.cnt || null;
    }

    /**
     * Returns a string representation of this operation
     */
    toString(): string {
        const parts: string[] = [];

        // type or action
        parts.push(this.action === null ? this.type : this.action);

        // operands
        if (this.p1 !== null) {
            parts.push(this.p1.toString());
            if (this.p2 !== null) {
                parts.push(", " + this.p2.toString());
            }
        }

        if (this.target !== null) {
            parts.push(this.target);
        }

        return parts.join(' ');
    }
}
