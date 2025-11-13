<script lang="ts">
    import {buildPath} from '../../libs/utils/url';

    let activeSection = $state('syntax-rules');

    const scrollToSection = (sectionId: string) => {
        activeSection = sectionId;
        const element = document.getElementById(sectionId);
        if (element) {
            // Scroll with offset to account for sticky header
            const headerHeight = 72; // Height of sticky header
            const offsetTop = element.getBoundingClientRect().top + window.scrollY - headerHeight - 20;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    };

    const navigationTree = [
        {
            id: 'syntax-rules', title: '语法规则', isParent: true,
            children: [
                {id: 'register', title: '寄存器'},
                {id: 'memory', title: '内存'},
                {id: 'instruction', title: '指令'},
                {id: 'code', title: '代码'},
            ]
        },
        {
            id: 'instructions', title: '指令说明', isParent: true,
            children: [
                {id: "op-mov", title: "mov"},
                {id: "op-add", title: "add"},
                {id: "op-sub", title: "sub"},
                {id: "op-mul", title: "mul"},
                {id: "op-div", title: "div"},
                {id: "op-cmp", title: "cmp"},
                {id: "op-jmp", title: "jmp je jne jg jge jl jle"},
                {id: "op-call", title: "call"},
                {id: "op-ret", title: "ret"},
                {id: "op-push", title: "push pushf"},
                {id: "op-pop", title: "pop popf"},
                {id: "op-nop", title: "nop"},
                {id: "op-input", title: "input"},
                {id: "op-print", title: "print println"},
                {id: "op-rand", title: "rand"},
                {id: "op-pause", title: "pause"},
                {id: "op-halt", title: "halt"},
            ]
        },
        {
            id: 'demos',
            title: '代码示例',
            isParent: true,
            children: [
                {id: 'demo-basic', title: '基本运算和输入输出'},
                {id: 'demo-jmp', title: '判断，跳转，循环'},
                {id: 'demo-call', title: '函数调用'},
                {id: 'demo-prime', title: '找质数'},
                {id: 'demo-fib', title: '斐波那契数列'},
                {id: 'demo-qsort', title: '快速排序'},
            ]
        },
    ];
</script>

<style>
    .manual-table {
        width: 100%;
        font-size: 0.8rem;
        border-collapse: collapse;
    }

    .manual-table td {
        border: 1px solid;
        padding: 0.25rem 0.5rem;
    }

</style>

<div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-blue-600 text-white p-4 shadow-md sticky top-0 z-10">
        <a href={buildPath('')}
           class="absolute left-2 top-1/2 -translate-y-1/2 flex items-center gap-2 hover:text-blue-200 transition-colors px-3 py-2 rounded-lg">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
            </svg>
            <span class="text-sm font-medium">Back</span>
        </a>
        <div class="container mx-auto relative">
            <div class="flex items-center justify-between">
                <h1 class="text-2xl font-bold flex items-center gap-3">
                    <img src="favicon.png" alt="Toy Computer" class="w-10 h-10 p-1 bg-white"/>
                    <span>Toy Computer Manual</span>
                </h1>
                <div class="flex gap-4">
                    <a href="https://github.com/goldenbull/toy-computer" target="_blank" rel="noopener noreferrer"
                       class="flex items-center gap-2 hover:text-blue-200 transition-colors">
                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path fill-rule="evenodd"
                                  d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
                                  clip-rule="evenodd"></path>
                        </svg>
                        <span class="text-sm font-medium">GitHub</span>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <div class="flex">
        <!-- Sidebar Navigation -->
        <aside class="w-64 bg-white shadow-lg h-[calc(100vh-72px)] sticky top-[72px] overflow-y-auto">
            <nav class="p-4">
                <ul class="space-y-1">
                    {#each navigationTree as item}
                        <li>
                            <button onclick={() => scrollToSection(item.id)}
                                    class={`w-full text-left px-3 py-2 rounded ${item.isParent ? 'font-semibold' : ''} ${activeSection === item.id ? 'bg-blue-100 text-blue-700 font-medium' : item.isParent ? 'text-gray-800 hover:bg-gray-100' : 'text-gray-700 hover:bg-gray-100'}`}>
                                {item.title}
                            </button>
                            {#if item.children}
                                <ul class="ml-4 mt-1 space-y-1">
                                    {#each item.children as child}
                                        <li>
                                            <button onclick={() => scrollToSection(child.id)}
                                                    class={`w-full text-left px-3 py-2 rounded text-sm ${activeSection === child.id ? 'bg-blue-100 text-blue-700 font-medium' : 'text-gray-600 hover:bg-gray-100'}`}>
                                                {child.title}
                                            </button>
                                        </li>
                                    {/each}
                                </ul>
                            {/if}
                        </li>
                    {/each}
                </ul>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 p-8 max-w-5xl font-mono">
            <section id="syntax-rules" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 border-b-2 border-blue-600 text-gray-800">语法规则</h2>

                <section id="register" class="mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">寄存器</h3>
                    <ol class="list-decimal list-inside space-y-3">
                        <li>通用寄存器：ax, bx, cx, dx</li>
                        <li>符号寄存器：flg</li>
                        <li>栈操作寄存器：bp, sp</li>
                        <li>指令寄存器：ip</li>
                    </ol>
                </section>

                <section id="memory" class="mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">内存</h3>
                    <p>内存有 1024 个单元，地址是从 0 到 1023 每个单元可以存一个数字，栈从 1023
                        开始从后往前生长，见示例中的斐波那契数列程序的执行过程</p>
                </section>

                <section id="instruction" class="mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">指令</h3>
                    <p>每条指令执行一个非常简单且明确的操作，具体见每条指令的详细说明</p>
                </section>

                <section id="code" class="mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">代码</h3>
                    <p class="mb-4">一个程序由若干条代码构成，代码的编写和执行规则如下：</p>
                    <ol class="list-decimal list-inside space-y-3">
                        <li> 所有指令和寄存器都使用小写字母，大写字母无法通过编译</li>
                        <li>
                            每个寄存器和每个内存单元可以类比为一个小盒子，里面只能放一个数，后放进去的数会覆盖之前的数。本系统只处理有符号整数，不处理浮点数，也不考虑字节长度等细节
                        </li>
                        <li>
                            每条指令可以有一个或多个label，作为跳转和函数调用的目标，label以字母和下划线(_)开头，可以包含字母、数字和下划线，以冒号结束
                        </li>
                        <li> 代码中可以有注释，以分号;开始注释，分号之后直到一行结束，都属于注释</li>
                        <li> 字符串首尾使用双引号，支持C风格的\转义</li>
                        <li> 系统执行代码时，永远从第一条指令开始，逐条往后执行，根据相应指令（jmp、call、ret）执行跳转，直到执行完最后一条指令，进入停机状态
                        </li>
                        <li> 代码需要首先经过Compile操作，Compile成功后才会加载到Execution面板，如果代码格式有错，Compile环节就会报错
                        </li>
                        <li>Compile成功后，系统进入初始状态，ip寄存器为0（即准备从第一条指令开始执行），栈寄存器初始化为1023，其他寄存器和内存都初始化为特殊值，方便观察和调试。（知道Visual
                            Studio “烫烫烫烫烫烫”的故事么？）
                        </li>
                        <li>可以通过Reset按钮重置系统，恢复初始状态</li>
                    </ol>
                </section>

            </section>

            <section id="instructions" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 border-b-2 border-blue-600 text-gray-800">指令说明</h2>
                <p class="mb-4">以下会用到的符号</p>
                <ul class="list-disc list-inside space-y-3">
                    <li> r1, r2: 表示寄存器</li>
                    <li> N: 表示一个整数</li>
                    <li> [r1 + N]:
                        表示内存中的一个位置，用寄存器的值加上偏移量N作为内存单元的编号，例如ax=10，那么[ax+5]就指向内存中第16个单元（0-base，第一个内存单元的地址是0）。
                        N可以是负数。N为0时可以简写为[r1]
                    </li>
                </ul>

                <section id="op-mov" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">mov</h3>
                    <p class="mb-4">赋值操作，给指定寄存器或者指定内存位置赋值，有以下几种格式：</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td> mov r1, N</td>
                            <td> 将数字 N 存入寄存器 r1 中</td>
                            <td> mov ax, 0</td>
                        </tr>
                        <tr>
                            <td> mov r1, r2</td>
                            <td> 将寄存器 r2 的值存入寄存器 r1 中，r2 本身保持不变</td>
                            <td><p>mov ax, bx</p>
                                <p>mov bp, sp</p></td>
                        </tr>
                        <tr>
                            <td> mov r1, [r2+N]</td>
                            <td> 将内存 [r2+N] 的值存入寄存器 r1 中，内存本身保持不变</td>
                            <td><p>mov ax, [bx]</p>
                                <p>mov ax, [bp+4]</p></td>
                        </tr>
                        <tr>
                            <td> mov [r1+N1], N2</td>
                            <td> 给内存单元赋值</td>
                            <td> mov [bp-2], 100</td>
                        </tr>
                        <tr>
                            <td> mov [r1+N], r2</td>
                            <td> 将寄存器 r2 的值写入内存</td>
                            <td> mov [bp+3], ax</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-add" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">add</h3>
                    <p class="mb-4">加法运算</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td> add r1, N</td>
                            <td> 将寄存器 r1 中的值和 N 相加，结果依然存入 r1 中，记做 r1 + N --> r1</td>
                            <td> add ax, 1</td>
                        </tr>
                        <tr>
                            <td> add r1, r2</td>
                            <td> r1 + r2 --> r1</td>
                            <td><p>add ax, bx</p>
                                <p>add sp, cx</p></td>
                        </tr>
                        <tr>
                            <td> add r1, [r2+N]</td>
                            <td> 将寄存器 r1 的值和内存 [r2+N] 的值相加，结果存入寄存器 r1 中，r1 + [r2+N] --> r1</td>
                            <td><p>add ax, [bx]</p>
                                <p>add ax, [bp+4]</p></td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-sub" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">sub</h3>
                    <p class="mb-4">减法运算</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td> sub r1, N</td>
                            <td> r1 - N --> r1</td>
                            <td> sub ax, 1</td>
                        </tr>
                        <tr>
                            <td> sub r1, r2</td>
                            <td> r1 - r2 --> r1</td>
                            <td><p>sub ax, bx</p>
                                <p>sub sp, cx</p></td>
                        </tr>
                        <tr>
                            <td> sub r1, [r2+N]</td>
                            <td> r1 - [r2+N] --> r1</td>
                            <td><p>sub ax, [bx]</p>
                                <p>sub ax, [bp+4]</p></td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-mul" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">mul</h3>
                    <p class="mb-4">乘法运算，固定使用寄存器 ax，将 ax 的值和指定值相乘，结果存入 ax</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>mul N</td>
                            <td>ax * N --> ax</td>
                            <td>mul 10</td>
                        </tr>
                        <tr>
                            <td>mul r1</td>
                            <td>ax * r1 --> ax</td>
                            <td>mul bx</td>
                        </tr>
                        <tr>
                            <td>mul [r1+N]</td>
                            <td>ax * [r1+N] --> ax</td>
                            <td>mul [bp+3]</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-div" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">div</h3>
                    <p class="mb-4">除法运算，固定使用ax作为被除数，将 ax 的值除以指定值，商存入 ax，余数存入 dx。
                        除法运算比较特殊，需要注意的几点：</p>
                    <ul class="list-disc list-inside space-y-3 mb-4">
                        <li>结果会占用两个寄存器，dx 保存余数，其原先的值会被覆盖</li>
                        <li>除数为0时，系统会报错，进入停机状态。事实上，除0操作的处理是CPU中很重要的一个技术。</li>
                        <li>余数不为0时，其符号和被除数相同</li>
                    </ul>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>div N</td>
                            <td>ax / N --> 商存入 ax，余数存入 dx</td>
                            <td><p>mov ax, 15</p>
                                <p>div -7</p></td>
                        </tr>
                        <tr>
                            <td>div r1</td>
                            <td>ax / r1，同上</td>
                            <td>div cx</td>
                        </tr>
                        <tr>
                            <td>div [r1+N]</td>
                            <td>ax / [r1+N]，同上</td>
                            <td>div [bp+3]</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-cmp" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">cmp</h3>
                    <p class="mb-4">比较运算，比较两个值的大小，结果存入 flg 寄存器</p>
                    <ul class="list-disc list-inside space-y-3 mb-4">
                        <li>第一个值大于第二个值时，flg = 1</li>
                        <li>第一个值等于第二个值时，flg = 0</li>
                        <li>第一个值小于第二个值时，flg = -1</li>
                    </ul>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>cmp r1, N</td>
                            <td>比较 r1 和 N，结果存入 flg</td>
                            <td>cmp ax, 0</td>
                        </tr>
                        <tr>
                            <td>cmp r1, r2</td>
                            <td>比较 r1 和 r2，结果存入 flg</td>
                            <td>cmp ax, bx</td>
                        </tr>
                        <tr>
                            <td>cmp r1, [r2+N]</td>
                            <td>比较 r1 和 [r2+N]，结果存入 flg</td>
                            <td>cmp cx, [bp+3]</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-jmp" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">jmp / je / jne / jg / jge / jl / jle</h3>
                    <p class="mb-4">跳转指令，根据 flg
                        寄存器的值决定是否跳转到指定标签。如果不跳转，则继续执行下一条指令。</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>jmp label</td>
                            <td>无条件跳转到 label</td>
                            <td>jmp _main</td>
                        </tr>
                        <tr>
                            <td>je label</td>
                            <td><span class="text-red-700">J</span>ump if <span class="text-red-700">E</span>qual,
                                如果 flg = 0（相等），跳转到 label
                            </td>
                            <td>
                                <p>; jump to _finish if cx is 0</p>
                                <p>cmp cx, 0</p>
                                <p>je _finish</p>
                            </td>
                        </tr>
                        <tr>
                            <td>jne label</td>
                            <td><span class="text-red-700">J</span>ump if <span class="text-red-700">N</span>ot <span
                                    class="text-red-700">E</span>qual,
                                如果 flg ≠ 0，跳转到 label
                            </td>
                            <td>
                                <p>; jump to _loop1 if cx is not 0</p>
                                <p>cmp cx, 0</p>
                                <p>jne _loop1</p>
                            </td>
                        </tr>
                        <tr>
                            <td>jg label</td>
                            <td><span class="text-red-700">J</span>ump if <span class="text-red-700">G</span>reater,
                                如果 flg > 0，跳转到 label
                            </td>
                            <td>
                                <p>; jump to _case1 if ax > bx</p>
                                <p>cmp ax, bx</p>
                                <p>jg _case1</p>
                            </td>
                        </tr>
                        <tr>
                            <td>jge label</td>
                            <td><span class="text-red-700">J</span>ump if <span class="text-red-700">G</span>reater or
                                <span class="text-red-700">E</span>qual,
                                如果 flg ≥ 0，跳转到 label
                            </td>
                            <td></td>
                        </tr>
                        <tr>
                            <td>jl label</td>
                            <td><span class="text-red-700">J</span>ump if <span class="text-red-700">L</span>ess,
                                如果 flg &lt; 0，跳转到 label
                            </td>
                            <td></td>
                        </tr>
                        <tr>
                            <td>jle label</td>
                            <td><span class="text-red-700">J</span>ump if <span class="text-red-700">L</span>ess or
                                <span class="text-red-700">E</span>qual,
                                如果 flg ≤ 0，跳转到 label
                            </td>
                            <td></td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-call" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">call</h3>
                    <p class="mb-4">函数调用，跳转到指定标签，并将返回地址（即当前ip寄存器+1）压入栈</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>call label</td>
                            <td>
                                <p>将下一条指令的地址压入栈，然后跳转到 label，即依次完成三个操作</p>
                                <ol class="list-decimal list-inside">
                                    <li> ip + 1 --> [sp]</li>
                                    <li> sp - 1 --> sp</li>
                                    <li> address of label --> ip</li>
                                </ol>
                            </td>
                            <td>
                                <p><span class="text-blue-500">_f1</span>: push bp</p>
                                <p> mov bp, sp</p>
                                <p> ...</p>
                                <p> call <span class="text-blue-500">_f1</span></p>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-ret" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">ret</h3>
                    <p class="mb-4">函数返回，从栈中弹出返回地址并跳转</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>ret</td>
                            <td>从栈中弹出返回地址，跳转回调用处，即依次完成两个操作
                                <ol class="list-decimal list-inside">
                                    <li> sp + 1 --> sp</li>
                                    <li> [sp] --> ip</li>
                                </ol>
                            </td>
                            <td>ret</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-push" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">push / pushf</h3>
                    <p class="mb-4">将值压入栈</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>push N</td>
                            <td>
                                <p>将数字 N 压入栈，即依次完成两个操作</p>
                                <ol class="list-decimal list-inside">
                                    <li> N --> [sp]</li>
                                    <li> sp - 1 --> sp</li>
                                </ol>
                            </td>
                            <td>push 100</td>
                        </tr>
                        <tr>
                            <td>push r1</td>
                            <td>将寄存器 r1 的值压入栈</td>
                            <td>push ax</td>
                        </tr>
                        <tr>
                            <td>push [r1+N]</td>
                            <td>将内存 [r1+N] 的值压入栈</td>
                            <td>push [bp+3]</td>
                        </tr>
                        <tr>
                            <td>pushf</td>
                            <td>将 flg 寄存器的值压入栈</td>
                            <td>pushf</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-pop" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">pop / popf</h3>
                    <p class="mb-4">从栈中弹出值</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>pop r1</td>
                            <td>
                                <p>从栈中弹出值，存入寄存器 r1，即依次完成两个操作</p>
                                <ol class="list-decimal list-inside">
                                    <li> sp + 1 --> sp</li>
                                    <li> [sp] --> r1</li>
                                </ol>
                            </td>
                            <td>pop ax</td>
                        </tr>
                        <tr>
                            <td>pop [r1+N]</td>
                            <td>从栈中弹出值，存入内存 [r1+N]</td>
                            <td>pop [bp-2]</td>
                        </tr>
                        <tr>
                            <td>popf</td>
                            <td>从栈中弹出值，存入 flg 寄存器</td>
                            <td>popf</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-nop" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">nop</h3>
                    <p class="mb-4"><span class="text-red-700">N</span>o <span class="text-red-700">Op</span>reation,
                        空操作指令，不执行任何操作，只是简单的执行ip+1</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>nop</td>
                            <td>不做任何操作，仅用于占位或调试</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-input" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">input</h3>
                    <p>输入操作，用户输入一个整数，存入指定位置。</p>
                    <p class="mb-4"> 从这条指令开始，后续的几条指令都是“伪指令”，即不存在于实际的汇编语言中，要通过复杂的函数才能实现线相应功能。
                        但出于教学目的，我们使用一条指令实现这些功能，以方便使用。
                    </p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>input r1</td>
                            <td>从用户获取输入，存入寄存器 r1</td>
                            <td>input ax</td>
                        </tr>
                        <tr>
                            <td>input [r1+N]</td>
                            <td>从用户获取输入，存入内存 [r1+N]</td>
                            <td>input [bp-2]</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-print" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">print / println</h3>
                    <p class="mb-4">
                        输出操作，将值输出到界面上。为了使用方便，有两个版本，print不会自动换行，而println会在输出的末尾自动换行</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>print N</td>
                            <td>输出数字 N（不换行）</td>
                            <td>print 100</td>
                        </tr>
                        <tr>
                            <td>print r1</td>
                            <td>输出寄存器 r1 的值（不换行）</td>
                            <td>print ax</td>
                        </tr>
                        <tr>
                            <td>print [r1+N]</td>
                            <td>输出内存 [r1+N] 的值（不换行）</td>
                            <td>print [bp+3]</td>
                        </tr>
                        <tr>
                            <td>print "字符串"</td>
                            <td>输出字符串（不换行）</td>
                            <td>print "Hello World!"</td>
                        </tr>
                        <tr>
                            <td>println</td>
                            <td>print line, 输出一个换行符，等价于 print "\n"</td>
                            <td>println</td>
                        </tr>
                        <tr>
                            <td>println N / r1 / [r1+N] / "字符串"</td>
                            <td>输出后自动换行</td>
                            <td><p>println ax</p>
                                <p>println "Hello World!"</p>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-rand" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">rand</h3>
                    <p class="mb-4">生成随机数（0-999），存入指定位置</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                            <td>示例</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>rand r1</td>
                            <td>生成随机数，存入寄存器 r1</td>
                            <td>rand ax</td>
                        </tr>
                        <tr>
                            <td>rand [r1+N]</td>
                            <td>生成随机数，存入内存 [r1+N]</td>
                            <td>rand [bp-2]</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-pause" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">pause</h3>
                    <p class="mb-4">暂停执行，切换到暂停状态</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>pause</td>
                            <td>暂停程序执行，可以通过 Continue 或 Step 按钮继续</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

                <section id="op-halt" class="mt-8 mb-12 ml-4">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">halt</h3>
                    <p class="mb-4">停机指令，终止程序执行</p>
                    <table class="manual-table">
                        <thead>
                        <tr>
                            <td>格式</td>
                            <td>说明</td>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>halt</td>
                            <td>停止程序执行，进入停机状态</td>
                        </tr>
                        </tbody>
                    </table>
                </section>

            </section>

            <section id="demos" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 border-b-2 border-blue-600 text-gray-800">代码示例</h2>
                <ul class="list-disc list-inside space-y-3 mb-4">
                    <li>
                        <a id="demo-basic" href="demo-basic.asm" class="text-green-700 hover:underline">
                            基本运算和输入输出 </a>
                    </li>
                    <li><a id="demo-jmp" href="demo-jmp.asm" class="text-green-700 hover:underline"> 判断，跳转，循环 </a>
                    </li>
                    <li><a id="demo-call" href="demo-call.asm" class="text-green-700 hover:underline"> 函数调用 </a>
                    </li>
                    <li><a id="demo-prime" href="demo-prime.asm" class="text-green-700 hover:underline"> 找质数 </a>
                    </li>
                    <li><a id="demo-fib" href="demo-fib.asm" class="text-green-700 hover:underline"> 斐波那契数列 </a>
                    </li>
                    <li><a id="demo-qsort" href="demo-qsort.asm" class="text-green-700 hover:underline"> 快速排序 </a>
                    </li>
                </ul>

            </section>

        </main>
    </div>
</div>

