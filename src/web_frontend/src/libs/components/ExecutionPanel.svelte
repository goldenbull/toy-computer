<script lang="ts">
    import {ExecStatus, MEMORY_SIZE} from '../ComputerStatus.svelte.ts';
    import {globalStatus, globalExecutor, setOutputScrollCallback} from '../store.svelte';
    import {onMount, onDestroy} from 'svelte';

    let {isDarkMode}: {
        isDarkMode: boolean
    } = $props();

    let outputTextarea: HTMLTextAreaElement;
    let operationsContainer: HTMLDivElement;
    let inputTextbox = $state<HTMLInputElement | null>(null);

    // Register output scroll callback when component mounts
    onMount(() => {
        setOutputScrollCallback(() => {
            if (outputTextarea) {
                requestAnimationFrame(() => {
                    outputTextarea.scrollTop = outputTextarea.scrollHeight;
                });
            }
        });
    });

    // Cleanup scroll callback on destroy
    onDestroy(() => {
        setOutputScrollCallback(null);
    });

    // Auto-scroll operations table to current IP
    // Smooth scroll only for step mode and reset (one click, one action)
    let useSmoothScroll = false;

    $effect(() => {
        const ip = globalStatus.registers.ip;
        if (operationsContainer && globalStatus.operations.length > 0) {
            // Capture and clear the smooth scroll flag
            const smooth = useSmoothScroll;
            useSmoothScroll = false;

            requestAnimationFrame(() => {
                const currentRow = operationsContainer.querySelector(`tr[data-addr="${ip}"]`) as HTMLElement;
                if (currentRow) {
                    const containerRect = operationsContainer.getBoundingClientRect();
                    const rowRect = currentRow.getBoundingClientRect();

                    // Calculate row's position relative to the visible container
                    const rowCenter = rowRect.top + rowRect.height / 2 - containerRect.top;
                    const containerHeight = containerRect.height;
                    const relativePosition = rowCenter / containerHeight;

                    // Only scroll if outside the [0.1, 0.9] range
                    if (relativePosition < 0.1 || relativePosition > 0.9) {
                        // Scroll to position the row at 0.1 of the container (better for forward execution)
                        const targetScrollTop = currentRow.offsetTop - containerHeight * 0.1 + rowRect.height / 2;
                        operationsContainer.scrollTo({
                            top: targetScrollTop,
                            behavior: smooth ? 'smooth' : 'instant'
                        });
                    }
                }
            });
        }
    });

    function runOneStep() {
        useSmoothScroll = true;
        globalExecutor.runOneStep();
    }

    async function runContinue() {
        await globalExecutor.runContinuous();
    }

    async function runAnimation() {
        // Execute with animation using the current speed setting
        await globalExecutor.runAnimation();
    }

    function runBreak() {
        globalExecutor.breakExecution();
    }

    function runReset() {
        useSmoothScroll = true;
        globalStatus.reset();
    }

    // Input dialog state
    let inputValue = $state('');
    let inputError = $state('');

    // Auto-focus input field when dialog appears
    $effect(() => {
        if (globalStatus.execStatus === ExecStatus.WaitingForInput && inputTextbox) {
            requestAnimationFrame(() => {
                if (inputTextbox) inputTextbox.focus();
            });
        }
    });

    async function handleInputSubmit() {
        try {
            inputError = '';
            globalExecutor.provideInput(inputValue);
            inputValue = '';

            // If status is Running after providing input, continue execution
            if (globalStatus.execStatus === ExecStatus.Running) {
                await globalExecutor.runContinuous();
            } else if (globalStatus.execStatus === ExecStatus.RunningAnimation) {
                await globalExecutor.runAnimation();
            }
        } catch (e) {
            // Only show input validation errors in the dialog
            // Execution errors (like invalid memory address) will be shown in output
            if (globalStatus.execStatus === ExecStatus.WaitingForInput) {
                inputError = e instanceof Error ? e.message : String(e);
            }
            // If dialog closed (status changed), the error is already in output, don't show in dialog
        }
    }

    function handleInputKeydown(event: KeyboardEvent) {
        if (event.key === 'Enter') {
            handleInputSubmit();
        } else if (event.key === 'Escape') {
            inputValue = '';
            inputError = '';
        }
    }
</script>

<style>
    .reg-table {
        width: 100%;
        font-size: 0.8rem;
        border-collapse: collapse;
    }

    .reg-cell {
        border: 1px solid #d1d5db;
        padding: 0.25rem 0.5rem;
    }

    .dark-reg-table .reg-cell {
        border-color: #4b5563;
    }

    .reg-name {
        font-weight: 500;
        width: 3rem;
        text-align: center;
    }

    .reg-value {
        min-width: 6rem;
        max-width: 8rem;
        text-align: right;
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none; /* IE and Edge */
    }

    /* Webkit (Chrome, Safari) */
    .reg-value::-webkit-scrollbar {
        display: none;
    }

    .mem-cell {
        position: relative;
        max-width: 5rem;
        overflow-x: auto;
        white-space: nowrap;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none; /* IE and Edge */
    }

    /* Webkit (Chrome, Safari) */
    .mem-cell::-webkit-scrollbar {
        display: none;
    }

    .mem-cell-dot-bp {
        position: absolute;
        top: 2px;
        left: 2px;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: #66cccc; /* green */
    }

    .mem-cell-dot-sp {
        position: absolute;
        top: 10px;
        left: 2px;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: #c084fc; /* purple */
    }

</style>

<!-- Main Layout: Two columns -->
<div class="flex gap-2 h-full {isDarkMode ? 'bg-gray-900' : ''} rounded">
    <!-- Left Column: Operations -->
    <div class="flex flex-col gap-2 w-1/4 min-h-0">
        <!-- Operations (flexible height with scroll) -->
        <div bind:this={operationsContainer}
             class="flex-1 overflow-auto p-2 rounded {isDarkMode ? 'bg-gray-800' : 'bg-white'}">
            {#if globalStatus.execStatus === ExecStatus.Running}
                <div class="flex items-center justify-center h-full">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-400 mx-auto mb-2"></div>
                        <p class="text-sm font-semibold {isDarkMode ? 'text-gray-300' : 'text-gray-700'}">运行中...</p>
                    </div>
                </div>
            {:else}
                {#if globalStatus.operations.length > 0}
                    <table class="w-full text-xs border-collapse font-mono {isDarkMode ? 'text-gray-200' : ''}">
                        <thead>
                        <tr class="sticky top-0 z-10 {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">
                            <th class="border px-1 py-1 text-center w-12 {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">
                                Addr
                            </th>
                            <th class="border px-1 py-1 text-center {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">
                                Code
                            </th>
                            <th class="border px-1 py-1 text-center w-16 {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">
                                Offset
                            </th>
                        </tr>
                        </thead>
                        <tbody>
                        {#each globalStatus.operations as op}
                            <tr data-addr={op.addr}
                                class={op.addr === globalStatus.registers.ip ? (isDarkMode ? 'bg-amber-700' : 'bg-amber-200') : ''}>
                                <td class="border px-1 py-1 text-right {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">{op.addr}</td>
                                <td class="border px-1 py-1 {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">
                                    {#each op.labels as label}
                                        <p class="font-semibold {isDarkMode ? 'text-blue-400' : 'text-blue-600'}">{label}:</p>
                                    {/each}
                                    <p class="px-4">{op.displayStr}</p>
                                </td>
                                <td class="border px-1 py-1 text-center {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">{op.offsetStr}</td>
                            </tr>
                        {/each}
                        </tbody>
                    </table>
                {:else}
                    <!-- no source code -->
                    <div class="flex items-center justify-center h-full">
                        <div class="text-center">
                            <p class="text-xl {isDarkMode ? 'text-gray-300' : ''}">代码尚未编译</p>
                        </div>
                    </div>
                {/if}

            {/if}
        </div>

        <!-- Control buttons -->
        <div class="flex flex-col gap-2 m-2">
            <!-- First row: Run, Run Animation, Animation speed -->
            <div class="flex gap-2">
                <button
                        class="flex-1 p-2 bg-green-600 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runContinue()}
                        disabled={globalStatus.execStatus!==ExecStatus.Ready&&globalStatus.execStatus!==ExecStatus.Paused}
                >
                    {globalStatus.execStatus === ExecStatus.Ready ? "启动" : "继续"}
                </button>

                <button
                        class="flex-1 p-2 bg-teal-600 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runAnimation()}
                        disabled={globalStatus.execStatus!==ExecStatus.Ready&&globalStatus.execStatus!==ExecStatus.Paused}
                >
                    {globalStatus.execStatus === ExecStatus.Ready ? "动画-启动" : "动画-继续"}
                </button>

                <div class="flex-1 flex p-2 flex-col gap-1">
                    <div class="flex justify-between text-xs {isDarkMode ? 'text-gray-400' : 'text-gray-600'}">
                        <span>Slow</span>
                        <span>Fast</span>
                    </div>
                    <input
                            id="speed-slider"
                            type="range"
                            min="0"
                            max="100"
                            step="1"
                            bind:value={globalExecutor.animationSpeed}
                            class="w-full h-2 rounded-lg appearance-none cursor-pointer accent-teal-600 {isDarkMode ? 'bg-gray-600' : 'bg-gray-200'}"
                    />
                </div>
            </div>
            <!-- Second row: Break, Step, Reset -->
            <div class="flex gap-2 items-center">
                <button
                        class="flex-1 p-2 bg-orange-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runBreak()}
                        disabled={globalStatus.execStatus!==ExecStatus.Running&&globalStatus.execStatus!==ExecStatus.RunningAnimation}
                >
                    中断
                </button>

                <button
                        class="flex-1 p-2 bg-blue-600 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runOneStep()}
                        disabled={globalStatus.execStatus!==ExecStatus.Ready&&globalStatus.execStatus!==ExecStatus.Paused}
                >
                    逐步
                </button>

                <button
                        class="flex-1 p-2 bg-red-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runReset()}
                        disabled={globalStatus.execStatus===ExecStatus.Running||globalStatus.execStatus===ExecStatus.RunningAnimation}
                >
                    Reset
                </button>
            </div>
        </div>
    </div>

    <!-- Right Column -->
    <div class="flex flex-col gap-2 w-full min-h-0">
        <!-- Top: Registers and Memory -->
        <div class="flex gap-2 h-1/2">
            {#if globalStatus.execStatus === ExecStatus.Running}
                <div class="flex items-center justify-center w-full">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-400 mx-auto mb-2"></div>
                        <p class="text-sm font-semibold {isDarkMode ? 'text-gray-300' : 'text-gray-700'}">运行中...</p>
                    </div>
                </div>
            {:else}
                <!-- Registers -->
                <div class="flex flex-col p-2 {isDarkMode ? 'text-gray-200' : ''}">

                    <table class="reg-table font-mono {isDarkMode ? 'dark-reg-table' : ''}">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-amber-700' : 'bg-amber-200'}">ip</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.ip}</td>
                        </tr>
                        </tbody>
                    </table>

                    <table class="mt-4 reg-table font-mono {isDarkMode ? 'dark-reg-table' : ''}">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">ax</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.ax}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">bx</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.bx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">cx</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.cx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">dx</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.dx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">flg</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.flg}</td>
                        </tr>
                        </tbody>
                    </table>

                    <table class="mt-4 reg-table font-mono {isDarkMode ? 'dark-reg-table' : ''}">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-teal-700' : 'bg-green-200'}">bp</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.bp}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name {isDarkMode ? 'bg-purple-700' : 'bg-purple-200'}">sp</td>
                            <td class="reg-cell reg-value">{globalStatus.registers.sp}</td>
                        </tr>
                        </tbody>
                    </table>

                </div>

                <!-- Memory (flexible width with scroll) -->
                <div class="flex-1 border rounded p-2 overflow-auto {isDarkMode ? 'border-gray-600 bg-gray-800' : 'border-gray-300 bg-white'}">
                    <div class="text-xs font-mono {isDarkMode ? 'text-gray-200' : ''}">
                        <table class="text-xs border-collapse">
                            <thead>
                            <tr class="sticky top-0 z-10 {isDarkMode ? 'bg-gray-700' : 'bg-gray-100'}">
                                <th class="border px-1 py-1 text-center {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">
                                    Addr
                                </th>
                                {#each Array(16) as _, col}
                                    <th class="border px-1 py-1 text-center w-16 {isDarkMode ? 'border-gray-600' : 'border-gray-300'}">
                                        +{col}</th>
                                {/each}
                            </tr>
                            </thead>
                            <tbody>
                            {#each Array(MEMORY_SIZE / 16) as _, row}
                                <tr>
                                    <td class="border px-1 py-1 text-center font-semibold {isDarkMode ? 'border-gray-600 bg-gray-700' : 'border-gray-300 bg-gray-100'}">{row * 16}</td>
                                    {#each Array(16) as _, col}
                                        {@const addr = row * 16 + col}
                                        {@const value = globalStatus.memory[addr]}
                                        {@const memType = globalStatus.getMemType(addr)}
                                        {@const isBpPointer = addr === globalStatus.registers.bp}
                                        {@const isSpPointer = addr === globalStatus.registers.sp}
                                        <td class="border px-1 py-1 text-right mem-cell {isDarkMode ? 'border-gray-600' : 'border-gray-300'}
                                    {memType === 'BP' ? (isDarkMode ? 'bg-teal-800' : 'bg-green-200') : ''}
                                    {memType === 'IP' ? (isDarkMode ? 'bg-amber-800' : 'bg-amber-200') : ''}">
                                            {#if isBpPointer}
                                                <span class="mem-cell-dot-bp"></span>
                                            {/if}
                                            {#if isSpPointer}
                                                <span class="mem-cell-dot-sp"></span>
                                            {/if}
                                            {value}
                                        </td>
                                    {/each}
                                </tr>
                            {/each}
                            </tbody>
                        </table>
                    </div>
                </div>
            {/if}
        </div>

        <!-- Output (flexible height) -->
        <div class="flex-1 border rounded me-1 mb-1 flex flex-col {isDarkMode ? 'border-gray-600 bg-gray-800' : 'border-gray-300 bg-white'}">
            <textarea
                    bind:this={outputTextarea}
                    class="grow w-full p-1 font-mono text-xs resize-none focus:outline-none border rounded
                           {isDarkMode ? 'bg-gray-900 text-gray-200 border-gray-600' : 'border-gray-200'}"
                    bind:value={globalStatus.output}
                    placeholder="Execution output appears here..."
                    readonly
            ></textarea>
        </div>
    </div>
</div>

<!-- Input Dialog Modal -->
{#if globalStatus.execStatus === ExecStatus.WaitingForInput}
    <div class="fixed inset-0 flex items-start justify-center pt-20 z-50 pointer-events-none">
        <div class="bg-white rounded-lg shadow-2xl border-2 border-blue-500 p-4 w-80 pointer-events-auto">
            <h3 class="text-base font-bold mb-2">等待输入</h3>
            <p class="text-xs text-gray-600 mb-2">
                输入整数赋值给 <span class="font-mono font-semibold">{globalStatus.inputTarget?.toString()}</span>:
            </p>
            <input
                    bind:this={inputTextbox}
                    type="text"
                    class="w-full px-2 py-1.5 text-sm border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
                    bind:value={inputValue}
                    onkeydown={handleInputKeydown}
                    placeholder="输入整数..."
            />
            {#if inputError}
                <p class="text-red-600 text-xs mt-1">{inputError}</p>
            {/if}
            <div class="flex gap-2 mt-3">
                <button
                        class="flex-1 py-1.5 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
                        onclick={handleInputSubmit}
                >
                    确定
                </button>
                <button
                        class="flex-1 py-1.5 text-sm bg-gray-400 text-white rounded hover:bg-gray-500"
                        onclick={() => { inputValue = ''; inputError = ''; }}
                >
                    清空
                </button>
            </div>
        </div>
    </div>
{/if}