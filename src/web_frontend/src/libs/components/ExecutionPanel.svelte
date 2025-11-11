<script lang="ts">
    import {type ComputerStatus, ExecStatus} from '../ComputerStatus.svelte.ts';
    import {WebExecutor} from '../WebExecutor';

    let {status}: {
        status: ComputerStatus
    } = $props();

    let executor = $state<WebExecutor | null>(null);

    // Create executor when operations are loaded
    $effect(() => {
        if (status.operations.length > 0) {
            executor = new WebExecutor(status);
        }
    });

    function runOneStep() {
        if (!executor) return;
        executor.runOneStep();
    }

    async function runContinue() {
        if (!executor) return;
        await executor.runContinuous();
    }

    function runBreak() {
        if (!executor) return;
        executor.breakExecution();
    }

    function runReset() {
        status.reset();
        if (status.operations.length > 0) {
            executor = new WebExecutor(status);
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
        padding: 0.25rem;
    }

    .reg-name {
        /*font-weight: 500;*/
        width: 2rem;
        text-align: center;
    }

    .reg-value {
        width: 4rem;
        text-align: right;
        font-family: monospace;
    }

</style>

<!-- Main Layout: Two columns -->
<div class="flex gap-2 h-[calc(100vh-200px)]">
    <!-- Left Column: Operations -->
    <div class="flex flex-col gap-2 w-1/4">
        <!-- Operations (flexible height with scroll) -->
        <div class="flex-1 bg-white overflow-auto p-2">
            {#if status.execStatus === ExecStatus.Running}
                <div class="flex items-center justify-center h-full">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-2"></div>
                        <p class="text-sm font-semibold text-gray-700">Running...</p>
                    </div>
                </div>
            {:else}
                <table class="w-full text-xs border-collapse font-mono">
                    <thead>
                    <tr class="bg-gray-100 sticky top-0">
                        <th class="border border-gray-300 px-1 py-1 text-center w-12">Addr</th>
                        <th class="border border-gray-300 px-1 py-1 text-left">Label & Op</th>
                        <th class="border border-gray-300 px-1 py-1 text-center w-16">Offset</th>
                    </tr>
                    </thead>
                    <tbody>
                    {#each status.operations as op}
                        {@const opString = op.toString()}
                        <tr class={op.addr === status.registers.ip ? 'bg-amber-200' : ''}>
                            <td class="border border-gray-300 px-1 py-1 text-right">{op.addr}</td>
                            <td class="border border-gray-300 px-1 py-1">
                                {#each op.labels as label}
                                    <p class="text-blue-600 font-semibold">{label}:</p>
                                {/each}
                                <p class="px-4">{opString}</p>
                            </td>
                            <td class="border border-gray-300 px-1 py-1 text-center">
                                {#if op.target && status.labels[op.target] !== undefined}
                                    {status.labels[op.target] - op.addr > 0 ? '+' : ''}{status.labels[op.target] - op.addr}
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
        <div class="flex gap-2">
            <button
                    class="flex-1 py-2 bg-green-600 text-white rounded disabled:cursor-not-allowed"
                    onclick={() => runContinue()}
                    disabled={status.execStatus!==ExecStatus.Ready&&status.execStatus!==ExecStatus.Paused}
            >
                Run
            </button>
            <button
                    class="flex-1 py-2 bg-blue-600 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed"
                    onclick={() => runOneStep()}
                    disabled={status.execStatus!==ExecStatus.Ready&&status.execStatus!==ExecStatus.Paused}
            >
                Step
            </button>
            <button
                    class="flex-1 py-2 bg-orange-500 text-white rounded disabled:cursor-not-allowed"
                    onclick={() => runBreak()}
                    disabled={status.execStatus!==ExecStatus.Running}
            >
                Break
            </button>
            <button
                    class="flex-1 py-2 bg-red-500 text-white rounded disabled:cursor-not-allowed"
                    onclick={() => runReset()}
                    disabled={status.execStatus===ExecStatus.Running}
            >
                Reset
            </button>
        </div>
    </div>

    <!-- Right Column -->
    <div class="flex flex-col gap-2 w-full">
        <!-- Top: Registers and Memory -->
        <div class="flex gap-2 h-1/2">
            {#if status.execStatus === ExecStatus.Running}
                <div class="flex items-center justify-center w-full">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-2"></div>
                        <p class="text-sm font-semibold text-gray-700">Running...</p>
                    </div>
                </div>
            {:else}
                <!-- Registers -->
                <div class="flex flex-col p-2">

                    <table class="reg-table">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name">ip</td>
                            <td class="reg-cell reg-value bg-amber-200">{status.registers.ip}</td>
                        </tr>
                        </tbody>
                    </table>

                    <table class="mt-4 reg-table">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name">ax</td>
                            <td class="reg-cell reg-value bg-gray-100">{status.registers.ax}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">bx</td>
                            <td class="reg-cell reg-value bg-gray-100">{status.registers.bx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">cx</td>
                            <td class="reg-cell reg-value bg-gray-100">{status.registers.cx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">dx</td>
                            <td class="reg-cell reg-value bg-gray-100">{status.registers.dx}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">flg</td>
                            <td class="reg-cell reg-value bg-gray-100">{status.registers.flg}</td>
                        </tr>
                        </tbody>
                    </table>

                    <table class="mt-4 reg-table">
                        <tbody>
                        <tr>
                            <td class="reg-cell reg-name">bp</td>
                            <td class="reg-cell reg-value bg-green-200">{status.registers.bp}</td>
                        </tr>
                        <tr>
                            <td class="reg-cell reg-name">sp</td>
                            <td class="reg-cell reg-value bg-purple-200">{status.registers.sp}</td>
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
                                        {@const value = status.memory[addr]}
                                        {@const memType = status.getMemType(addr)}
                                        <td class="border border-gray-300 px-1 py-1 text-right
                                    {memType === 'BP' ? 'bg-green-200' : ''}
                                    {memType === 'IP' ? 'bg-amber-200' : ''}
                                    {addr === status.registers.sp ? 'bg-purple-200' : ''}">
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
                    class="flex-grow w-full p-2 font-mono text-xs resize-none focus:outline-none border border-gray-200 rounded"
                    bind:value={status.output}
                    placeholder="Execution output appears here..."
                    readonly
            ></textarea>
        </div>
    </div>
</div>