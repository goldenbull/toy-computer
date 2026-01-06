<script lang="ts">
    import {ExecStatus} from '../ComputerStatus.svelte.ts';
    import {globalStatus, globalExecutor, setOutputScrollCallback} from '../store.svelte';
    import {onMount} from 'svelte';

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

    // Auto-scroll operations table to current IP
    $effect(() => {
        const ip = globalStatus.registers.ip;
        if (operationsContainer && globalStatus.operations.length > 0) {
            requestAnimationFrame(() => {
                const currentRow = operationsContainer.querySelector(`tr[data-addr="${ip}"]`);
                if (currentRow) {
                    currentRow.scrollIntoView({behavior: 'smooth', block: 'center'});
                }
            });
        }
    });

    function runOneStep() {
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

    .reg-name {
        font-weight: 500;
        width: 3rem;
        text-align: center;
    }

    .reg-value {
        min-width: 4rem;
        text-align: right;
    }

</style>

<!-- Main Layout: Two columns -->
<div class="flex gap-2 h-full">
    <!-- Left Column: Operations -->
    <div class="flex flex-col gap-2 w-1/4">
        <!-- Operations (flexible height with scroll) -->
        <div bind:this={operationsContainer} class="flex-1 bg-white overflow-auto p-2">
            {#if globalStatus.execStatus === ExecStatus.Running}
                <div class="flex items-center justify-center h-full">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-2"></div>
                        <p class="text-sm font-semibold text-gray-700">后台运行中...</p>
                    </div>
                </div>
            {:else}
                <table class="w-full text-xs border-collapse font-mono">
                    <thead>
                    <tr class="bg-gray-100 sticky top-0">
                        <th class="border border-gray-300 px-1 py-1 text-center w-12">Addr</th>
                        <th class="border border-gray-300 px-1 py-1 text-center">Code</th>
                        <th class="border border-gray-300 px-1 py-1 text-center w-16">Offset</th>
                    </tr>
                    </thead>
                    <tbody>
                    {#each globalStatus.operations as op}
                        {@const opString = op.toString()}
                        <tr data-addr={op.addr} class={op.addr === globalStatus.registers.ip ? 'bg-amber-200' : ''}>
                            <td class="border border-gray-300 px-1 py-1 text-right">{op.addr}</td>
                            <td class="border border-gray-300 px-1 py-1">
                                {#each op.labels as label}
                                    <p class="text-blue-600 font-semibold">{label}:</p>
                                {/each}
                                <p class="px-4">{opString}</p>
                            </td>
                            <td class="border border-gray-300 px-1 py-1 text-center">
                                {#if op.target && globalStatus.labels[op.target] !== undefined}
                                    {globalStatus.labels[op.target] - op.addr > 0 ? '+' : ''}{globalStatus.labels[op.target] - op.addr}
                                {:else}
                                    {""}
                                {/if}
                            </td>
                        </tr>
                    {/each}
                    </tbody>
                </table>
            {/if}
        </div>

        <!-- Control buttons -->
        <div class="flex flex-col gap-2">
            <!-- First row: Run, Run Animation, Step -->
            <div class="flex gap-2">
                <button
                        class="flex-1 p-2 bg-teal-600 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runAnimation()}
                        disabled={globalStatus.execStatus!==ExecStatus.Ready&&globalStatus.execStatus!==ExecStatus.Paused}
                >
                    {globalStatus.execStatus === ExecStatus.Ready ? "动画-启动" : "动画-继续"}
                </button>
                <button
                        class="flex-1 p-2 bg-green-600 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runContinue()}
                        disabled={globalStatus.execStatus!==ExecStatus.Ready&&globalStatus.execStatus!==ExecStatus.Paused}
                >
                    {globalStatus.execStatus === ExecStatus.Ready ? "后台-启动" : "后台-继续"}
                </button>
                <button
                        class="flex-1 p-2 bg-blue-600 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runOneStep()}
                        disabled={globalStatus.execStatus!==ExecStatus.Ready&&globalStatus.execStatus!==ExecStatus.Paused}
                >
                    逐步
                </button>
            </div>
            <!-- Second row: Animation Speed, Break, Reset -->
            <div class="flex gap-2 items-center">
                <div class="flex-1 flex flex-col gap-1">
                    <div class="flex justify-between text-xs text-gray-600">
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
                            class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-teal-600"
                    />
                </div>
                <button
                        class="flex-1 py-2 bg-orange-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runBreak()}
                        disabled={globalStatus.execStatus!==ExecStatus.Running&&globalStatus.execStatus!==ExecStatus.RunningAnimation}
                >
                    中断
                </button>
                <button
                        class="flex-1 py-2 bg-red-500 text-white rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
                        onclick={() => runReset()}
                        disabled={globalStatus.execStatus===ExecStatus.Running||globalStatus.execStatus===ExecStatus.RunningAnimation}
                >
                    Reset
                </button>
            </div>
        </div>
    </div>

    <!-- Right Column -->
    <div class="flex flex-col gap-2 w-full">
        <!-- Top: Registers and Memory -->
        <div class="flex gap-2 h-1/2">
            {#if globalStatus.execStatus === ExecStatus.Running}
                <div class="flex items-center justify-center w-full">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-2"></div>
                        <p class="text-sm font-semibold text-gray-700">后台运行中...</p>
                    </div>
                </div>
            {:else}
                <!-- Registers -->
                <div class="flex flex-col p-2">

                    <table class="reg-table font-mono">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name">ip</td>
                            <td class="reg-cell reg-value bg-amber-200">{globalStatus.registers.ip}</td>
                        </tr>
                        </tbody>
                    </table>

                    <table class="mt-4 reg-table font-mono">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name">ax</td>
                            <td class="reg-cell reg-value bg-gray-100">{globalStatus.registers.ax}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">bx</td>
                            <td class="reg-cell reg-value bg-gray-100">{globalStatus.registers.bx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">cx</td>
                            <td class="reg-cell reg-value bg-gray-100">{globalStatus.registers.cx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">dx</td>
                            <td class="reg-cell reg-value bg-gray-100">{globalStatus.registers.dx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">flg</td>
                            <td class="reg-cell reg-value bg-gray-100">{globalStatus.registers.flg}</td>
                        </tr>
                        </tbody>
                    </table>

                    <table class="mt-4 reg-table font-mono">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name">bp</td>
                            <td class="reg-cell reg-value bg-green-200">{globalStatus.registers.bp}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">sp</td>
                            <td class="reg-cell reg-value bg-purple-200">{globalStatus.registers.sp}</td>
                        </tr>
                        </tbody>
                    </table>

                </div>

                <!-- Memory (flexible width with scroll) -->
                <div class="flex-1 border border-gray-300 rounded p-2 bg-white overflow-auto">
                    <div class="text-xs font-mono">
                        <table class="text-xs border-collapse">
                            <thead>
                            <tr class="bg-gray-100 sticky top-0">
                                <th class="border border-gray-300 px-1 py-1 text-center">Addr</th>
                                {#each Array(16) as _, col}
                                    <th class="border border-gray-300 px-1 py-1 text-center w-16">+{col}</th>
                                {/each}
                            </tr>
                            </thead>
                            <tbody>
                            {#each Array(1024 / 16) as _, row}
                                <tr>
                                    <td class="border border-gray-300 px-1 py-1 text-center bg-gray-100 font-semibold">{row * 16}</td>
                                    {#each Array(16) as _, col}
                                        {@const addr = row * 16 + col}
                                        {@const value = globalStatus.memory[addr]}
                                        {@const memType = globalStatus.getMemType(addr)}
                                        <td class="border border-gray-300 px-1 py-1 text-right
                                    {memType === 'BP' ? 'bg-green-200' : ''}
                                    {memType === 'IP' ? 'bg-amber-200' : ''}
                                    {addr === globalStatus.registers.sp ? 'bg-purple-200' : ''}">
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
        <div class="flex-1 border border-gray-300 rounded p-2 bg-white flex flex-col">
            <h3 class="font-bold mb-2 text-sm">Output</h3>
            <textarea
                    bind:this={outputTextarea}
                    class="flex-grow w-full p-2 font-mono text-xs resize-none focus:outline-none border border-gray-200 rounded"
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