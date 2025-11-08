<script lang="ts">
    import {onMount} from 'svelte';
    import SourceCodeEditor from '../libs/components/SourceCodeEditor.svelte';
    import ExecutionPanel from '../libs/components/ExecutionPanel.svelte';
    import {ComputerStatus} from '../libs/ComputerStatus';

    // global computer status object
    let status = new ComputerStatus();

    let activeTab = 'editor';
    const switchTab = (tab: string) => {
        activeTab = tab;
    };

    async function runCode(stepMode: boolean) {
        if (status.isRunning) {
            // TODO: ask if stop the running code
            return;
        }

        status.stepMode = stepMode;
        status.isRunning = true;

        // TODO: switch to execution panel and start
    }

</script>

<div class="min-h-screen flex flex-col">
    <header class="bg-blue-600 text-white p-4 shadow-md">
        <div class="container mx-auto">
            <h1 class="text-2xl font-bold">Toy Computer Simulator</h1>
        </div>
    </header>

    <main class="container-fluid p-2 flex-grow">
        <div class="bg-white rounded-lg shadow-lg overflow-hidden flex flex-col h-full">
            <!-- Tab Navigation -->
            <div class="flex border-b">
                <button
                        class={`p-3 font-medium text-sm ${activeTab === 'editor' ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
                        on:click={() => switchTab('editor')}
                >
                    Source Code Editor
                </button>
                <button
                        class={`px-6 py-3 font-medium text-sm ${activeTab === 'status' ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
                        on:click={() => switchTab('status')}
                >
                    Execution Status
                </button>
            </div>

            <!-- Tab Content -->
            <div class="p-2 flex-grow">
                <!-- Editor Tab -->
                {#if activeTab === 'editor'}
                    <SourceCodeEditor
                            status={status}
                            runCode={runCode}/>
                {/if}

                <!-- Execution Status Tab -->
                {#if activeTab === 'status'}
                    <ExecutionPanel status={status}/>
                {/if}
            </div>
        </div>

        <div class="mt-6 text-sm text-gray-600">
            <p><span class="font-semibold">Note:</span> footer message here </p>
        </div>
    </main>
</div>
