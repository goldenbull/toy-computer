<script lang="ts">
    import CodeMirror from "svelte-codemirror-editor";
    import {globalStatus} from '../store.svelte';
    import {buildApiUrl} from '../utils/url';

    let {switchTab}: {
        switchTab: (tab: string) => void
    } = $props();

    let errorMessage = $state<string>('');
    let showErrorModal = $state(false);
    let fileInput: HTMLInputElement;

    const loadSourceCode = () => {
        // Trigger file input click
        fileInput.click();
    };

    const handleFileLoad = (event: Event) => {
        const target = event.target as HTMLInputElement;
        const file = target.files?.[0];

        if (!file) return;

        const reader = new FileReader();
        reader.onload = (e) => {
            const content = e.target?.result as string;
            if (content) {
                globalStatus.sourceCode = content;
            }
        };
        reader.readAsText(file);

        // Reset input so the same file can be loaded again
        target.value = '';
    };

    async function compileCode() {
        // Compile the source code by calling the backend API
        try {
            const apiUrl = buildApiUrl('api/compile');
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    sourceCode: globalStatus.sourceCode
                })
            });

            const result = await response.json();

            if (!result.success) {
                // Compilation error - show in modal
                errorMessage = result.error;
                showErrorModal = true;
                return;
            }

            // Load the compiled operations
            globalStatus.loadCompiledCode(result.operations, result.labels);

            // Switch to execution panel
            switchTab('execution');
        } catch (error) {
            errorMessage = `Error: ${error}`;
            showErrorModal = true;
        }
    }

    function closeErrorModal() {
        showErrorModal = false;
    }

</script>

<div class="flex flex-col h-full flex-grow">
    <!-- Hidden file input -->
    <input
            type="file"
            bind:this={fileInput}
            onchange={handleFileLoad}
            accept=".asm,.txt"
            class="hidden"
    />

    <div class="flex-grow border border-gray-300 rounded-lg overflow-hidden relative">
        <CodeMirror bind:value={globalStatus.sourceCode}
                    class="w-full h-full p-4 font-mono text-sm resize-none focus:outline-none absolute inset-0"
                    placeholder="Enter your assembly code here..."
                    styles={{"&": {height: "100%", overflow: "auto"}}}
        />
    </div>

    <div class="mt-4 flex space-x-2">
        <button class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700" onclick={compileCode}>
            Compile
        </button>
        <button class="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700" onclick={loadSourceCode}>
            Load Source Code
        </button>
    </div>
</div>

<!-- Error Modal -->
{#if showErrorModal}
    <div
            class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
            onclick={closeErrorModal}
            onkeydown={(e) => e.key === 'Escape' && closeErrorModal()}
            role="button"
            tabindex="0"
            aria-label="Close modal"
    >
        <div
                class="bg-white rounded-lg shadow-xl max-w-2xl w-full mx-4 max-h-[80vh] overflow-auto"
                role="dialog"
                aria-modal="true"
                aria-labelledby="error-modal-title"
                tabindex="-1"
                onclick={(e) => e.stopPropagation()}
                onkeydown={(e) => e.stopPropagation()}
        >
            <div class="bg-red-600 text-white px-6 py-4 rounded-t-lg">
                <h3 id="error-modal-title" class="text-lg font-bold">Compilation Error</h3>
            </div>
            <div class="p-6">
                <pre class="bg-gray-100 p-4 rounded text-sm font-mono whitespace-pre-wrap break-words">{errorMessage}</pre>
            </div>
            <div class="px-6 py-4 bg-gray-50 rounded-b-lg flex justify-end">
                <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700" onclick={closeErrorModal}>
                    Close
                </button>
            </div>
        </div>
    </div>
{/if}