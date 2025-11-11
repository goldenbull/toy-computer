<script lang="ts">
    import {onMount} from 'svelte';
    import SourceCodeEditor from '../libs/components/SourceCodeEditor.svelte';
    import ExecutionPanel from '../libs/components/ExecutionPanel.svelte';
    import {ComputerStatus} from '../libs/ComputerStatus.svelte.ts';

    // global computer status object
    let status = $state(new ComputerStatus());

    let activeTab = $state('editor');
    const switchTab = (tab: string) => {
        activeTab = tab;
    };
</script>

<div class="min-h-screen flex flex-col">
    <header class="bg-blue-600 text-white p-4 shadow-md">
        <div class="container mx-auto">
            <h1 class="text-2xl font-bold flex items-center gap-3">
                <img src="/favicon.png" alt="Toy Computer" class="w-10 h-10 p-1 bg-white"/>
                <span>Toy Computer Simulator</span>
            </h1>
        </div>
    </header>

    <main class="container-fluid p-2 flex-grow">
        <div class="bg-white rounded-lg shadow-lg overflow-hidden flex flex-col h-full">
            <!-- Tab Navigation -->
            <div class="flex border-b">
                <button
                        class={`p-3 font-medium text-sm ${activeTab === 'editor' ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
                        onclick={() => switchTab('editor')}
                >
                    Source Code Editor
                </button>
                <button
                        class={`px-6 py-3 font-medium text-sm ${activeTab === 'execution' ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
                        onclick={() => switchTab('execution')}
                >
                    Execution
                </button>
            </div>

            <!-- Tab Content -->
            <div class="p-2 flex-grow">
                <!-- Editor Tab -->
                {#if activeTab === 'editor'}
                    <SourceCodeEditor bind:status={status} switchTab={switchTab}/>
                {/if}

                <!-- Execution Panel Tab -->
                {#if activeTab === 'execution'}
                    <ExecutionPanel status={status}/>
                {/if}
            </div>
        </div>

        <div class="mt-6 text-sm text-gray-600">
            <p><span class="font-semibold">Note:</span> footer message here </p>
        </div>
    </main>
</div>
