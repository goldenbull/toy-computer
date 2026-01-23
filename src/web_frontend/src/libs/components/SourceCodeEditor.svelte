<script lang="ts">
    import CodeMirror from "svelte-codemirror-editor";
    import {EditorView} from '@codemirror/view';
    import {HighlightStyle, syntaxHighlighting} from '@codemirror/language';
    import {Prec} from '@codemirror/state';
    import {tags} from '@lezer/highlight';
    import {globalStatus} from '../store.svelte';
    import {Compiler, CompileError} from '../Compiler';
    import {toyAsm} from '../toyAsmLanguage';
    import {coolGlow, ayuLight} from 'thememirror';

    // Custom highlight for dark mode - numbers in yellow
    const darkNumberHighlight = Prec.highest(syntaxHighlighting(HighlightStyle.define([
        {tag: tags.number, color: '#facc15'}
    ])));

    // Custom highlight for light mode - numbers in green
    const lightNumberHighlight = Prec.highest(syntaxHighlighting(HighlightStyle.define([
        {tag: tags.number, color: '#0533eb'},
        {tag: tags.labelName, color: '#303030'},
        {tag: tags.keyword, color: '#d060d0'},
        {tag: tags.variableName, color: '#40b030'},
    ])));

    let {switchTab, isDarkMode}: {
        switchTab: (tab: string) => void,
        isDarkMode: boolean
    } = $props();

    let errorMessage = $state<string>('');
    let showErrorModal = $state(false);
    let editorView = $state<EditorView | null>(null);
    let errorInfo = $state<CompileError | null>(null);

    const currentTheme = $derived(
        isDarkMode
            ? [coolGlow, darkNumberHighlight]
            : [ayuLight, lightNumberHighlight]
    );
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
        const blob = new Blob([globalStatus.sourceCode], {type: 'text/plain'});

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
            errorInfo = result.firstError;
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

        // Move cursor to error position
        if (editorView && errorInfo) {
            const doc = editorView.state.doc;
            const line = doc.line(errorInfo.lineNum + 1); // lineNum is 0-based, doc.line is 1-based
            const pos = line.from + errorInfo.column;
            editorView.dispatch({
                selection: {anchor: pos},
                effects: EditorView.scrollIntoView(pos, {y: 'center'})
            });
            editorView.focus();
        }
    }

</script>

<div class="flex flex-col h-full grow">
    <!-- Hidden file input -->
    <input
            type="file"
            bind:this={fileInput}
            onchange={handleFileLoad}
            accept=".asm,.txt"
            class="hidden"
    />

    <div class="grow border border-gray-300 rounded-lg overflow-hidden relative">
        <CodeMirror bind:value={globalStatus.sourceCode}
                    class="w-full h-full p-4 font-mono text-sm resize-none focus:outline-none absolute inset-0"
                    placeholder="Enter your assembly code here..."
                    styles={{"&": {height: "100%", overflow: "auto"}}}
                    lang={toyAsm}
                    theme={currentTheme}
                    onready={(view) => editorView = view}
        />
    </div>

    <div class="mt-4 flex space-x-2">
        <button class="px-4 py-2 w-40 bg-green-600 text-white rounded hover:bg-green-700" onclick={compileCode}>
            编译
        </button>
        <button class="px-4 py-2 w-40 bg-blue-600 text-white rounded hover:bg-blue-700" onclick={saveSourceCode}>
            保存到文件
        </button>
        <button class="px-4 py-2 bg-sky-600 text-white rounded hover:bg-gray-700" onclick={loadSourceCode}>
            读入asm或txt文件
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
                <pre class="bg-gray-100 p-4 rounded text-sm font-mono whitespace-pre-wrap wrap-break-word">{errorMessage}</pre>
            </div>
            <div class="px-6 py-4 bg-gray-50 rounded-b-lg flex justify-end">
                <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700" onclick={closeErrorModal}>
                    Close
                </button>
            </div>
        </div>
    </div>
{/if}