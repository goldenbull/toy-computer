export class ComputerStatus {
    sourceCode: string = `; Example program: calculate 1 + 2
mov ax, 1
add ax, 2
print ax
println
halt
`;

    output: string = '';

    isRunning: boolean = false;
    stepMode: boolean = false;
    halted: boolean = false;

    registers = {
        ax: 0,
        bx: 0,
        cx: 0,
        dx: 0,
        flg: 0,
        sp: 1023,
        bp: 1023,
        ip: 0,
    };
}