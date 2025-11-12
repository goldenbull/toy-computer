<script lang="ts">
    import SourceCodeEditor from '../libs/components/SourceCodeEditor.svelte';
    import ExecutionPanel from '../libs/components/ExecutionPanel.svelte';
    import {globalStatus, STORAGE_KEY} from '../libs/store.svelte';

    let activeTab = $state('editor');
    const switchTab = (tab: string) => {
        activeTab = tab;
    };

    // Save source code to localStorage whenever it changes
    $effect(() => {
        if (globalStatus.sourceCode) {
            localStorage.setItem(STORAGE_KEY, globalStatus.sourceCode);
        }
    });
</script>

<div class="min-h-screen flex flex-col">
    <header class="bg-blue-600 text-white p-4 shadow-md">
        <div class="container mx-auto flex items-center justify-between">
            <h1 class="text-2xl font-bold flex items-center gap-3">
                <img src="favicon.png" alt="Toy Computer" class="w-10 h-10 p-1 bg-white"/>
                <span>Toy Computer Simulator</span>
            </h1>
            <a href="https://github.com/goldenbull/toy-computer" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 hover:text-blue-200 transition-colors">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                    <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
                </svg>
                <span class="text-sm font-medium">GitHub</span>
            </a>
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
                    <SourceCodeEditor switchTab={switchTab}/>
                {/if}

                <!-- Execution Panel Tab -->
                {#if activeTab === 'execution'}
                    <ExecutionPanel/>
                {/if}
            </div>
        </div>
    </main>
</div>
