<script lang="ts">
    import CodeMirror from "svelte-codemirror-editor";
    import {globalStatus} from '../store.svelte';
    import {Compiler} from '../Compiler';
    import {toyAsm} from '../toyAsmLanguage';
    import {coolGlow, ayuLight} from 'thememirror';

    let {switchTab}: {
        switchTab: (tab: string) => void
    } = $props();

    let errorMessage = $state<string>('');
    let showErrorModal = $state(false);
    let isDarkMode = $state(true);

    const currentTheme = $derived(isDarkMode ? coolGlow : ayuLight);
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

    const saveSourceCode = () => {
        // Create a blob with the source code content
        const blob = new Blob([globalStatus.sourceCode], { type: 'text/plain' });

        // Create a temporary URL for the blob
        const url = URL.createObjectURL(blob);

        // Create a temporary anchor element and trigger download
        const a = document.createElement('a');
        a.href = url;
        a.download = 'source.asm';
        document.body.appendChild(a);
        a.click();

        // Clean up
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    };

    function compileCode() {
        const compiler = new Compiler();
        const result = compiler.compile(globalStatus.sourceCode);

        if (!result.success) {
            // Compilation error - show in modal
            errorMessage = result.firstError?.toString() ?? '未知错误';
            showErrorModal = true;
            return;
        }

        // Load the compiled operations
        globalStatus.loadCompiledCode(result.operations, result.labels);

        // Switch to execution panel
        switchTab('execution');
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
                    lang={toyAsm}
                    theme={currentTheme}
        />
    </div>

    <div class="mt-4 flex">
        <div class="flex space-x-2">
            <button class="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700" onclick={loadSourceCode}>
                从本地加载
            </button>
            <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700" onclick={saveSourceCode}>
                保存到本地
            </button>
            <button class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700" onclick={compileCode}>
                编译
            </button>
        </div>

        <!-- Theme toggle buttons -->
        <div class="ml-auto flex space-x-1">
            <button
                class="px-3 py-1 text-sm rounded transition-colors {isDarkMode ? 'bg-gray-700 text-white' : 'bg-gray-200 text-gray-500 hover:bg-gray-300'}"
                onclick={() => isDarkMode = true}
            >
                Dark
            </button>
            <button
                class="px-3 py-1 text-sm rounded transition-colors {!isDarkMode ? 'bg-amber-100 text-amber-800' : 'bg-gray-200 text-gray-500 hover:bg-gray-300'}"
                onclick={() => isDarkMode = false}
            >
                Light
            </button>
        </div>
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