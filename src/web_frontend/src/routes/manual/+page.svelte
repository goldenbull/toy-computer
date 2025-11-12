<script lang="ts">
    let activeSection = $state('syntax-rules');

    const scrollToSection = (sectionId: string) => {
        activeSection = sectionId;
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({behavior: 'smooth'});
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
            id: 'instructions', title: '指令汇总', isParent: true,
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
                {id: "op-input", title: "input"},
                {id: "op-print", title: "print println"},
                {id: "op-rand", title: "rand"},
                {id: "op-dump", title: "dump"},
                {id: "op-pause", title: "pause"},
                {id: "op-halt", title: "halt"},
                {id: "op-nop", title: "nop"},
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
                {id: 'demo-sort', title: '排序'},
            ]
        },
    ];
</script>

<div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-blue-600 text-white p-4 shadow-md sticky top-0 z-10">
        <a href="../"
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
        <main class="flex-1 p-8 max-w-5xl">
            <section id="intro" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 text-gray-800">介绍</h2>
                <p class="text-gray-700 mb-4">用于计算机编程的入门教学。</p>
                <p class="text-gray-700">
                    引入一个极度简化、抽象后的计算机模型，只包含最简单的CPU和内存，逐步引入各条ASM汇编指令。</p>
            </section>

            <section id="basic-rules" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 text-gray-800">最基本的规则</h2>
                <ol class="list-decimal list-inside space-y-3 text-gray-700">
                    <li>整个系统只有几个概念：指令、CPU、寄存器、数字、内存</li>
                    <li>
                        指令：程序的最基本单位，一条语句就是一个指令，由CPU负责执行，每条指令的执行逻辑都是极度简单、清晰、明确的，指令的语句全部使用小写，每条指令前还可以有一个或多个自定义的标签
                    </li>
                    <li>用分号;开始注释，等同于C语言的//和python语言的#</li>
                    <li>CPU、寄存器
                        <ul class="list-disc list-inside ml-6 mt-2 space-y-1">
                            <li>
                                CPU负责执行指令，具体执行指令的细节涉及到很低层的数字电路了，不是这里要解决的问题，因此执行过程可以简化，只需要抽象了解加减乘除等基本运算等逻辑就可以。
                            </li>
                            <li>寄存器在CPU内部，每个寄存器是一个小格子，可以存一个数字，要强调寄存器的"临时"性质</li>
                        </ul>
                    </li>
                    <li>数字：只处理有符号整数，不考虑浮点数，也不考虑不同长度的整型</li>
                    <li>内存，用来保存数据和指令，分为数据内存和指令内存
                        <ul class="list-disc list-inside ml-6 mt-2 space-y-1">
                            <li>
                                数据内存由1024个小格子组成，和寄存器一样，每个格子也可以存一个数字，所有格子顺序编号，0-base
                            </li>
                            <li>指令内存也是一堆小格子，每个格子一条指令，也顺序编号，且每条指令可以有一个自定义的label
                            </li>
                            <li>内存和寄存器的区别：内存比寄存器慢100倍，但量大便宜</li>
                        </ul>
                    </li>
                    <li>教学时的类比：
                        <ul class="list-disc list-inside ml-6 mt-2 space-y-1">
                            <li>指令内存和指令：操作手册，每一步的操作（不可擦写）</li>
                            <li>数据内存：黑板（面积大，可擦写）</li>
                            <li>寄存器：草稿纸（面积小，可擦写）</li>
                            <li>CPU：操作员，人</li>
                        </ul>
                    </li>
                </ol>
            </section>

            <section id="lessons" class="mb-12">
                <h2 class="text-3xl font-bold mb-6 text-gray-800 pb-3 border-b-2 border-blue-600">Lessons</h2>

                <section id="lesson-1" class="mb-12 ml-4">
                    <h2 class="text-3xl font-bold mb-4 text-gray-800">Lesson 1 - 寄存器的简单操作</h2>
                    <p class="text-gray-700 mb-4"><strong>核心概念：</strong>寄存器的赋值和算术运算</p>
                    <p class="text-gray-700 mb-4">引入4个通用寄存器：<code
                            class="bg-gray-100 px-2 py-1 rounded">ax</code>
                        <code class="bg-gray-100 px-2 py-1 rounded">bx</code> <code
                                class="bg-gray-100 px-2 py-1 rounded">cx</code> <code
                                class="bg-gray-100 px-2 py-1 rounded">dx</code>
                    </p>

                    <div class="overflow-x-auto">
                        <table class="min-w-full bg-white border border-gray-300">
                            <thead>
                            <tr class="bg-gray-100">
                                <th class="px-4 py-2 border">指令</th>
                                <th class="px-4 py-2 border">格式</th>
                                <th class="px-4 py-2 border">含义</th>
                                <th class="px-4 py-2 border">样例</th>
                            </tr>
                            </thead>
                            <tbody class="text-gray-700">
                            <tr>
                                <td class="px-4 py-2 border font-mono">mov</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov r1, N</td>
                                <td class="px-4 py-2 border">将数字N存入寄存器r1中</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov ax, 0<br/>mov bx, 100</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border"></td>
                                <td class="px-4 py-2 border font-mono text-sm">mov r1, r2</td>
                                <td class="px-4 py-2 border">将寄存器r2的值存入寄存器r1中<br/>r1被覆盖，r2保持不变</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov ax, bx</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">add</td>
                                <td class="px-4 py-2 border font-mono text-sm">add r1, N</td>
                                <td class="px-4 py-2 border">将数字N和寄存器r1中的数字相加<br/>结果依然存入r1中</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov ax, 1<br/>add ax, 2<br/>;此时ax=3
                                </td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border"></td>
                                <td class="px-4 py-2 border font-mono text-sm">add r1, r2</td>
                                <td class="px-4 py-2 border">将寄存器r1和r2中的数字相加<br/>结果存入r1中，r2保持不变</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov ax, 1<br/>mov bx, 2<br/>add ax,
                                    bx<br/>;此时ax=3，bx=2
                                </td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">sub</td>
                                <td class="px-4 py-2 border font-mono text-sm">sub r1, N<br/>sub r1, r2</td>
                                <td class="px-4 py-2 border">减法 r1-N → r1<br/>r1-r2 → r1</td>
                                <td class="px-4 py-2 border"></td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">mul</td>
                                <td class="px-4 py-2 border font-mono text-sm">mul N</td>
                                <td class="px-4 py-2 border">乘数必须预先放入ax中<br/>ax*N → ax</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov ax, 3<br/>mul 4<br/>;此时ax=12</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border"></td>
                                <td class="px-4 py-2 border font-mono text-sm">mul r1</td>
                                <td class="px-4 py-2 border">ax*r1 → ax</td>
                                <td class="px-4 py-2 border"></td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">div</td>
                                <td class="px-4 py-2 border font-mono text-sm">div N</td>
                                <td class="px-4 py-2 border">
                                    整数除法，被除数必须预先放入ax中<br/>商在ax中，余数在dx中<br/>余数始终和ax符号相同
                                </td>
                                <td class="px-4 py-2 border font-mono text-sm">mov ax, 11<br/>div 4<br/>;此时ax=2, dx=3
                                </td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">input</td>
                                <td class="px-4 py-2 border font-mono text-sm">input r1</td>
                                <td class="px-4 py-2 border">用户输入一个数字，存入r1中</td>
                                <td class="px-4 py-2 border font-mono text-sm">input ax</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">print</td>
                                <td class="px-4 py-2 border font-mono text-sm">print N<br/>print r1<br/>print "STR"<br/>println
                                    ...
                                </td>
                                <td class="px-4 py-2 border">输出数字或字符串<br/>println在末尾自动换行</td>
                                <td class="px-4 py-2 border font-mono text-sm">print cx<br/>println "hello"</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">rand</td>
                                <td class="px-4 py-2 border font-mono text-sm">rand r1</td>
                                <td class="px-4 py-2 border">生成[0, 999]范围内的随机数存入r1</td>
                                <td class="px-4 py-2 border font-mono text-sm">rand ax</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4">
                        <h4 class="font-bold text-blue-800 mb-2">练习任务</h4>
                        <ol class="list-decimal list-inside space-y-1 text-gray-700">
                            <li>从1加到10，输出结果</li>
                            <li>输入两个数，输出两个数的加减乘除的各种结果</li>
                        </ol>
                    </div>
                </section>

                <section id="lesson-2" class="mb-12 ml-4">
                    <h2 class="text-3xl font-bold mb-4 text-gray-800">Lesson 2 - 内存操作</h2>
                    <p class="text-gray-700 mb-4"><strong>核心概念：</strong>按地址读写内存，变量</p>
                    <p class="text-gray-700 mb-4">内存统一通过 <code
                            class="bg-gray-100 px-2 py-1 rounded">[寄存器+偏移量]</code> 的格式访问，偏移量为0时可省略，也可以为负数。
                    </p>

                    <div class="overflow-x-auto mb-4">
                        <table class="min-w-full bg-white border border-gray-300">
                            <thead>
                            <tr class="bg-gray-100">
                                <th class="px-4 py-2 border">指令</th>
                                <th class="px-4 py-2 border">格式</th>
                                <th class="px-4 py-2 border">样例</th>
                            </tr>
                            </thead>
                            <tbody class="text-gray-700">
                            <tr>
                                <td class="px-4 py-2 border font-mono">mov</td>
                                <td class="px-4 py-2 border font-mono text-sm">mov [r1+N1], N2<br/>mov [r1+N], r2<br/>mov
                                    r1, [r2+N]
                                </td>
                                <td class="px-4 py-2 border font-mono text-sm">mov cx, 1<br/>mov [cx], 123<br/>;将123存入内存[1]
                                </td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">add/sub</td>
                                <td class="px-4 py-2 border font-mono text-sm">add r1, [r2+N]<br/>sub r1, [r2+N]</td>
                                <td class="px-4 py-2 border"></td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">mul/div</td>
                                <td class="px-4 py-2 border font-mono text-sm">mul [r1+N]<br/>div [r1+N]</td>
                                <td class="px-4 py-2 border"></td>
                            </tr>
                            </tbody>
                        </table>
                    </div>

                    <h3 class="text-xl font-bold mb-3 text-gray-800">调试指令</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full bg-white border border-gray-300">
                            <thead>
                            <tr class="bg-gray-100">
                                <th class="px-4 py-2 border">指令</th>
                                <th class="px-4 py-2 border">格式</th>
                                <th class="px-4 py-2 border">含义</th>
                            </tr>
                            </thead>
                            <tbody class="text-gray-700">
                            <tr>
                                <td class="px-4 py-2 border font-mono">dump</td>
                                <td class="px-4 py-2 border font-mono text-sm">dump<br/>dump r1, N<br/>dump N1, N2</td>
                                <td class="px-4 py-2 border">输出当前计算机运行状态<br/>可选显示内存区域</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">halt</td>
                                <td class="px-4 py-2 border font-mono text-sm">halt</td>
                                <td class="px-4 py-2 border">立即结束运行，进入停机状态</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">pause</td>
                                <td class="px-4 py-2 border font-mono text-sm">pause</td>
                                <td class="px-4 py-2 border">暂停，回车后继续运行</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">nop</td>
                                <td class="px-4 py-2 border font-mono text-sm">nop</td>
                                <td class="px-4 py-2 border">no operation，CPU空转一次</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4">
                        <h4 class="font-bold text-blue-800 mb-2">练习任务</h4>
                        <p class="text-gray-700">输入4个数，然后依次输出：这4个数本身的值，4个数的和、平方和</p>
                    </div>
                </section>

                <section id="lesson-3" class="mb-12 ml-4">
                    <h2 class="text-3xl font-bold mb-4 text-gray-800">Lesson 3 - 循环，判断，跳转</h2>
                    <p class="text-gray-700 mb-4"><strong>核心概念：</strong>条件控制，跳转，理解使用变量作为下标访问数组
                    </p>

                    <h3 class="text-xl font-bold mb-3 text-gray-800">跳转指令</h3>
                    <p class="text-gray-700 mb-4">引入寄存器 <code class="bg-gray-100 px-2 py-1 rounded">flg</code>（只能通过cmp指令写入）和
                        <code class="bg-gray-100 px-2 py-1 rounded">ip</code>（指令指针）</p>

                    <div class="overflow-x-auto">
                        <table class="min-w-full bg-white border border-gray-300">
                            <thead>
                            <tr class="bg-gray-100">
                                <th class="px-4 py-2 border">指令</th>
                                <th class="px-4 py-2 border">格式</th>
                                <th class="px-4 py-2 border">含义</th>
                            </tr>
                            </thead>
                            <tbody class="text-gray-700">
                            <tr>
                                <td class="px-4 py-2 border font-mono">jmp</td>
                                <td class="px-4 py-2 border font-mono text-sm">jmp label</td>
                                <td class="px-4 py-2 border">无条件跳转到label</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">cmp</td>
                                <td class="px-4 py-2 border font-mono text-sm">cmp r1, N<br/>cmp r1, r2<br/>cmp r1,
                                    [r2+N]
                                </td>
                                <td class="px-4 py-2 border">比较大小，结果存入flg<br/>r1>N → flg=1<br/>r1==N →
                                    flg=0<br/>r1&lt;N
                                    → flg=-1
                                </td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">je</td>
                                <td class="px-4 py-2 border font-mono text-sm">je label</td>
                                <td class="px-4 py-2 border">jump if equal（flg=0则跳转）</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">jne</td>
                                <td class="px-4 py-2 border font-mono text-sm">jne label</td>
                                <td class="px-4 py-2 border">jump if not equal（flg≠0则跳转）</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">jg</td>
                                <td class="px-4 py-2 border font-mono text-sm">jg label</td>
                                <td class="px-4 py-2 border">jump if greater（flg>0则跳转）</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">jge</td>
                                <td class="px-4 py-2 border font-mono text-sm">jge label</td>
                                <td class="px-4 py-2 border">jump if greater or equal（flg≥0则跳转）</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">jl</td>
                                <td class="px-4 py-2 border font-mono text-sm">jl label</td>
                                <td class="px-4 py-2 border">jump if less（flg&lt;0则跳转）</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">jle</td>
                                <td class="px-4 py-2 border font-mono text-sm">jle label</td>
                                <td class="px-4 py-2 border">jump if less or equal（flg≤0则跳转）</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4">
                        <h4 class="font-bold text-blue-800 mb-2">练习任务</h4>
                        <ol class="list-decimal list-inside space-y-1 text-gray-700 text-sm">
                            <li>从1加到10，输出结果</li>
                            <li>输入一个数N，从1加到N，输出结果</li>
                            <li>输出斐波那契数列的前100项</li>
                            <li>输入一个数，判断这个数是否是7的倍数</li>
                            <li>输入一个数，判断这个数的十进制表达里面是否包含7</li>
                            <li>输入一个数，判断是否是质数</li>
                            <li>输出10000以内的所有质数</li>
                            <li>孪生质数问题：找出10000以内的所有孪生质数（N和N+2都是质数）</li>
                        </ol>
                    </div>
                </section>

                <section id="lesson-4" class="mb-12 ml-4">
                    <h2 class="text-3xl font-bold mb-4 text-gray-800">Lesson 4 - 函数</h2>
                    <p class="text-gray-700 mb-4"><strong>核心概念：</strong>函数调用和返回，栈的基本使用</p>

                    <h3 class="text-xl font-bold mb-3 text-gray-800">栈和新寄存器</h3>
                    <p class="text-gray-700 mb-4">引入寄存器 <code class="bg-gray-100 px-2 py-1 rounded">sp</code>（栈指针）和
                        <code class="bg-gray-100 px-2 py-1 rounded">bp</code>（基指针）</p>
                    <ul class="list-disc list-inside space-y-2 text-gray-700 mb-4">
                        <li><strong>sp (stack pointer):</strong> 记录下一个空闲的栈位置，初始值为1023，向下增长</li>
                        <li><strong>bp (base pointer):</strong> 记录当前函数栈帧的起点</li>
                        <li><strong>栈:</strong> 内存后部专用于栈，前部为堆（heap）</li>
                    </ul>

                    <div class="overflow-x-auto mb-4">
                        <table class="min-w-full bg-white border border-gray-300">
                            <thead>
                            <tr class="bg-gray-100">
                                <th class="px-4 py-2 border">指令</th>
                                <th class="px-4 py-2 border">格式</th>
                                <th class="px-4 py-2 border">含义</th>
                            </tr>
                            </thead>
                            <tbody class="text-gray-700">
                            <tr>
                                <td class="px-4 py-2 border font-mono">push</td>
                                <td class="px-4 py-2 border font-mono text-sm">push N<br/>push r1</td>
                                <td class="px-4 py-2 border">将值压入栈，sp自动减1</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">pop</td>
                                <td class="px-4 py-2 border font-mono text-sm">pop r1<br/>pop</td>
                                <td class="px-4 py-2 border">从栈中弹出值，sp自动加1</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">call</td>
                                <td class="px-4 py-2 border font-mono text-sm">call label</td>
                                <td class="px-4 py-2 border">将返回地址(ip)压栈并跳转</td>
                            </tr>
                            <tr>
                                <td class="px-4 py-2 border font-mono">ret</td>
                                <td class="px-4 py-2 border font-mono text-sm">ret</td>
                                <td class="px-4 py-2 border">从栈中恢复ip并返回</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4">
                        <h4 class="font-bold text-blue-800 mb-2">练习任务</h4>
                        <ol class="list-decimal list-inside space-y-1 text-gray-700">
                            <li>将Lesson 3的任务改用函数实现</li>
                            <li>生成100个随机数，使用非递归排序算法排序</li>
                            <li>使用 <code class="bg-gray-100 px-1 rounded">--step</code> 模式观察函数调用前后栈和寄存器的变化
                            </li>
                        </ol>
                    </div>
                </section>

                <section id="lesson-5" class="mb-12 ml-4">
                    <h2 class="text-3xl font-bold mb-4 text-gray-800">Lesson 5 - 参数、返回值、局部变量</h2>
                    <p class="text-gray-700 mb-4"><strong>核心概念：</strong>函数 Stack Frame 的运行机制</p>

                    <h3 class="text-xl font-bold mb-3 text-gray-800">Stack Frame 布局</h3>
                    <p class="text-gray-700 mb-4">以函数 f1(a, b) = a+b+1 为例，栈帧布局如下（栈向下生长）：</p>

                    <div class="bg-gray-100 p-4 rounded font-mono text-sm mb-4">
                        <div class="border-l-2 border-gray-400 pl-4">
                            <div>b ; 第二个参数 &lt;-- sp在调用前</div>
                            <div>a ; 第一个参数</div>
                            <div>r ; 返回值槽位</div>
                            <div>ip ; call指令压入的返回地址</div>
                            <div>bp ; 保存的前一个frame的bp</div>
                            <div>x1 ; 局部变量1 &lt;-- bp指向此处</div>
                            <div>x2 ; 局部变量2</div>
                            <div> ; &lt;-- sp指向此处（下一个可用位置）</div>
                        </div>
                    </div>

                    <h3 class="text-xl font-bold mb-3 text-gray-800">调用示例</h3>
                    <div class="bg-gray-800 text-gray-100 p-4 rounded font-mono text-sm mb-4">
                        <div class="text-green-400">; 调用函数</div>
                        <div>push ax <span class="text-gray-500">; 第一个参数</span></div>
                        <div>push bx <span class="text-gray-500">; 第二个参数</span></div>
                        <div>sub sp, 1 <span class="text-gray-500">; 为返回值预留位置</span></div>
                        <div>call _f1</div>
                        <div>mov ax, [sp+1] <span class="text-gray-500">; 获取返回值</span></div>
                        <div>add sp, 3 <span class="text-gray-500">; 清理栈</span></div>
                        <div class="mt-4"></div>
                        <div class="text-green-400">; 函数实现</div>
                        <div>_f1:</div>
                        <div> push bp</div>
                        <div> mov bp, sp</div>
                        <div> mov ax, [bp+4] <span class="text-gray-500">; 第一个参数</span></div>
                        <div> mov bx, [bp+5] <span class="text-gray-500">; 第二个参数</span></div>
                        <div> add ax, bx</div>
                        <div> add ax, 1</div>
                        <div> mov [bp+3], ax <span class="text-gray-500">; 写入返回值</span></div>
                        <div> mov sp, bp</div>
                        <div> pop bp</div>
                        <div> ret</div>
                    </div>

                    <div class="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4">
                        <h4 class="font-bold text-blue-800 mb-2">练习任务</h4>
                        <ol class="list-decimal list-inside space-y-1 text-gray-700">
                            <li>使用 <code class="bg-gray-100 px-1 rounded">--step</code> 模式观察上述代码执行过程中栈和寄存器的变化
                            </li>
                            <li>使用递归函数实现斐波那契数列，观察递归调用和返回过程</li>
                        </ol>
                    </div>
                </section>

                <section id="lesson-6" class="mb-12 ml-4">
                    <h2 class="text-3xl font-bold mb-4 text-gray-800">Lesson 6 - 大实验：排序算法</h2>
                    <p class="text-gray-700 mb-4">
                        到目前为止，一个抽象意义上的计算机已经功能齐全了，可以实现复杂的算法。</p>

                    <div class="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4">
                        <h4 class="font-bold text-blue-800 mb-2">练习任务</h4>
                        <ul class="list-disc list-inside space-y-1 text-gray-700">
                            <li>随机生成100个数，存到内存里，将其排序，输出排序前后的结果</li>
                            <li>可以先使用交换排序、冒泡排序等非递归算法</li>
                            <li>实现递归的快速排序</li>
                        </ul>
                    </div>
                </section>

            </section>

            <section id="registers" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 text-gray-800">寄存器汇总</h2>
                <div class="overflow-x-auto">
                    <table class="min-w-full bg-white border border-gray-300">
                        <thead>
                        <tr class="bg-gray-100">
                            <th class="px-4 py-2 border">类型</th>
                            <th class="px-4 py-2 border">寄存器</th>
                            <th class="px-4 py-2 border">说明</th>
                        </tr>
                        </thead>
                        <tbody class="text-gray-700">
                        <tr>
                            <td class="px-4 py-2 border">通用寄存器</td>
                            <td class="px-4 py-2 border font-mono">ax, bx, cx, dx</td>
                            <td class="px-4 py-2 border">可用于任意操作</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2 border">符号寄存器</td>
                            <td class="px-4 py-2 border font-mono">flg</td>
                            <td class="px-4 py-2 border">只能通过cmp或popf赋值，存储比较结果</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2 border">指令寄存器</td>
                            <td class="px-4 py-2 border font-mono">ip</td>
                            <td class="px-4 py-2 border">指令指针，初始化为0，不能用mov修改</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2 border">栈寄存器</td>
                            <td class="px-4 py-2 border font-mono">sp, bp</td>
                            <td class="px-4 py-2 border">sp初始化为1023，用于栈操作，需遵循规范</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <section id="instructions" class="mb-12">
                <h2 class="text-3xl font-bold mb-4 text-gray-800">指令汇总</h2>
                <div class="space-y-6">
                    <div>
                        <h3 class="text-lg font-semibold mb-2 text-gray-800">数据传送</h3>
                        <p class="font-mono text-sm text-gray-700">mov, push, pop</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold mb-2 text-gray-800">算术运算</h3>
                        <p class="font-mono text-sm text-gray-700">add, sub, mul, div</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold mb-2 text-gray-800">比较与跳转</h3>
                        <p class="font-mono text-sm text-gray-700">cmp, jmp, je, jne, jg, jge, jl, jle</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold mb-2 text-gray-800">函数调用</h3>
                        <p class="font-mono text-sm text-gray-700">call, ret</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold mb-2 text-gray-800">输入输出</h3>
                        <p class="font-mono text-sm text-gray-700">input, print, println, rand</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-semibold mb-2 text-gray-800">调试控制</h3>
                        <p class="font-mono text-sm text-gray-700">dump, halt, pause, nop</p>
                    </div>
                </div>

                <div class="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-4">
                    <h4 class="font-bold text-yellow-800 mb-2">程序语法</h4>
                    <ul class="list-disc list-inside space-y-1 text-gray-700">
                        <li>用分号 <code class="bg-gray-100 px-1 rounded">;</code> 表示注释</li>
                        <li>每一行一条指令，指令全部小写</li>
                        <li>指令可以有标签，标签可以单独占一行</li>
                        <li>标签格式：小写字母加冒号，如 <code class="bg-gray-100 px-1 rounded">loop1:</code></li>
                    </ul>
                </div>
            </section>

            <div class="mt-12 pt-8 border-t border-gray-300 text-center text-gray-600">
                <p>使用 <code class="bg-gray-100 px-2 py-1 rounded">-s</code> 或 <code
                        class="bg-gray-100 px-2 py-1 rounded">--step</code> 参数可以进入逐行模式</p>
                <p class="mt-2">每执行一条指令，就会自动执行一次 <code class="bg-gray-100 px-2 py-1 rounded">dump</code>
                </p>
            </div>
        </main>
    </div>
</div>

<style>
    code {
        font-family: 'Monaco', 'Courier New', monospace;
    }
</style>
