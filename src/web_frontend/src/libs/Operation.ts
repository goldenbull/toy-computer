import {Operand} from './Operand';

export class Operation {
    addr: number;
    type: string;
    labels: string[];
    p1: Operand | null;
    p2: Operand | null;
    action: string | null;
    target: string | null;
    cnt: number | null;

    constructor(data: any) {
        this.addr = data.addr;
        this.type = data.type;
        this.labels = data.labels || [];
        this.p1 = data.p1 ? new Operand(data.p1) : null;
        this.p2 = data.p2 ? new Operand(data.p2) : null;
        this.action = data.action || null;
        this.target = data.target || null;
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

        // special for dump
        if (this.type == 'dump') {
            parts.length = 1;
            if (this.p1) {
                parts.push(this.p1.toString() + ",");
                parts.push(String(this.cnt));
            }
        }

        return parts.join(' ');
    }
}
