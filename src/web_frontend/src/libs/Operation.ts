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

        // Add type
        parts.push(this.type);

        // Add operands based on operation type
        switch (this.type) {
            case 'move':
            case 'add':
            case 'sub':
            case 'cmp':
                if (this.p1 && this.p2) {
                    parts.push(this.p1.toString() + ",");
                    parts.push(this.p2.toString());
                }
                break;

            case 'mul':
            case 'div':
            case 'input':
            case 'rand':
                if (this.p1) {
                    parts.push(this.p1.toString());
                }
                break;

            case 'jump':
                if (this.action && this.target) {
                    return `${this.action} ${this.target}`;
                }
                break;

            case 'call':
                if (this.target) {
                    parts.push(this.target);
                }
                break;

            case 'push':
            case 'pop':
            case 'print':
                if (this.action) {
                    parts[0] = this.action;
                }
                if (this.p1) {
                    parts.push(this.p1.toString());
                }
                break;

            case 'dump':
                if (this.p1) {
                    parts.push(this.p1.toString());
                    if (this.cnt !== null) {
                        parts.push(String(this.cnt));
                    }
                }
                break;

            case 'ret':
            case 'pause':
            case 'halt':
            case 'nop':
                // No operands
                break;
        }

        return parts.join(' ');
    }

    /**
     * Returns a display string with labels and address
     */
    toDisplayString(): string {
        let result = '';

        // Add labels if any
        if (this.labels.length > 0) {
            result += this.labels.join(', ') + ':\n';
        }

        // Add address and instruction
        result += `[${this.addr}] ${this.toString()}`;

        return result;
    }
}
