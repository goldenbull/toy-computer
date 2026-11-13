<script lang="ts">
    import CodeMirror from "svelte-codemirror-editor";
    import {EditorView} from '@codemirror/view';
    import {linter, lintGutter} from '@codemirror/lint';
    import {HighlightStyle, syntaxHighlighting} from '@codemirror/language';
    import {Prec} from '@codemirror/state';
    import {tags} from '@lezer/highlight';
    import {onDestroy} from 'svelte';
    import {globalStatus} from '../store.svelte';
    import {Compiler, CompileError} from '../Compiler';
    import {toyAsm} from '../toyAsmForCodemirror.ts';
    import {coolGlow, ayuLight} from 'thememirror';

    // Custom highlight for dark mode - numbers in yellow
    const darkNumberHighlight = Prec.highest(syntaxHighlighting(HighlightStyle.define([
        {tag: tags.number, color: '#facc15'}
    ])));

    // Custom highlight for light mode - numbers in green
    const lightNumberHighlight = Prec.highest(syntaxHighlighting(HighlightStyle.define([
        {tag: tags.number, color: '#0533eb'},
        {tag: tags.labelName, color: '#202020'},
        {tag: tags.keyword, color: '#d060d0'},
        {tag: tags.variableName, color: '#40b030'},
        {tag: tags.comment, color: '#909090'},
    ])));

    let {switchTab, isDarkMode}: {
        switchTab: (tab: string) => void,
        isDarkMode: boolean
    } = $props();

    let diagnostics = $state<CompileError[]>([]);
    const diagnosticExtensions = [lintGutter(), linter(view => {
        diagnostics = new Compiler().compile(view.state.doc.toString()).errors;
        return diagnostics.map(error => {
            const line = view.state.doc.line(error.lineNum + 1);
            const from = Math.min(line.to, line.from + error.column);
            return {from, to: Math.min(line.to, from + error.length), severity: 'error' as const, message: error.message};
        });
    }, {delay: 350})];

    function goToError(error: CompileError) {
        if (!editorView) return;
        const doc = editorView.state.doc;
        const line = doc.line(Math.min(error.lineNum + 1, doc.lines));
        const pos = Math.min(line.to, line.from + error.column);
        editorView.dispatch({selection: {anchor: pos}, effects: EditorView.scrollIntoView(pos, {y: 'center'})});
        editorView.focus();
    }

    let errorMessage = $state<string>('');
    let showErrorModal = $state(false);
    let editorView = $state<EditorView | null>(null);
    let errorInfo = $state<CompileError | null>(null);

    const gutterLayout = Prec.highest(EditorView.theme({
        '.cm-lineNumbers .cm-gutterElement': {
            minWidth: '2ch',
            padding: '0 4px'
        },
        '.cm-gutter-lint': {width: '1.5em'},
        '.cm-line': {paddingLeft: '8px'}
    }));
    const darkGutter = Prec.highest(EditorView.theme({
        '.cm-gutters': {
            backgroundColor: '#171a30',
            color: '#929bb5',
            borderRight: '1px solid #303650'
        },
        '.cm-activeLineGutter': {backgroundColor: '#29304b', color: '#e2e8f0'}
    }));
    const lightGutter = Prec.highest(EditorView.theme({
        '.cm-gutters': {
            backgroundColor: '#edf0f5',
            color: '#64748b',
            borderRight: '1px solid #cbd5e1'
        },
        '.cm-activeLineGutter': {backgroundColor: '#dbe5f2', color: '#1e293b'}
    }));

    const currentTheme = $derived(
        isDarkMode
            ? [coolGlow, darkNumberHighlight, gutterLayout, darkGutter]
            : [ayuLight, lightNumberHighlight, gutterLayout, lightGutter]
    );
    let fileInput: HTMLInputElement;

    // Cleanup editor reference on destroy
    onDestroy(() => {
        editorView = null;
    });

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
            if (typeof content === 'string') {
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
        const result = new Compiler().compile(globalStatus.sourceCode);

        if (!result.success) {
            // Compilation error - show in modal
            diagnostics = result.errors;
            errorMessage = result.errors.map(error => error.toString()).join('\n\n');
            errorInfo = result.firstError;
            showErrorModal = true;
            return;
        }

        // Load the compiled operations
        globalStatus.loadCompiledCode(result.operations);

        // Switch to execution panel
        switchTab('execution');
    }

    function closeErrorModal() {
        showErrorModal = false;

        if (errorInfo) goToError(errorInfo);
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
                    class="w-full h-full p-2 font-mono text-sm resize-none focus:outline-none absolute inset-0"
                    placeholder="Enter your assembly code here..."
                    styles={{"&": {height: "100%", overflow: "auto"}}}
                    lang={toyAsm}
                    extensions={diagnosticExtensions}
                    foldGutter={false}
                    closeBrackets={true}
                    autocompletion={true}
                    theme={currentTheme}
                    onready={(view) => editorView = view}
        />
    </div>

    {#if diagnostics.length}
        <div class="text-sm px-3 py-1 text-gray-700" role="status" aria-live="polite">
            发现 {diagnostics.length} 处错误，点击下方条目定位
        </div>
        <ul class="max-h-40 overflow-auto border-t border-red-200 bg-red-50 text-red-900 text-sm" aria-label="代码错误">
            {#each diagnostics as error}
                <li><button class="w-full text-left px-3 py-2 hover:bg-red-100 whitespace-pre-wrap" onclick={() => goToError(error)}>第 {error.lineNum + 1} 行，第 {error.column + 1} 列：{error.message}</button></li>
            {/each}
        </ul>
    {/if}
    <div class="mt-2 ml-6 flex space-x-4">
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
                <h3 id="error-modal-title" class="text-lg font-bold">编译失败</h3>
            </div>
            <div class="p-6">
                <pre class="text-gray-900 bg-gray-100 p-4 rounded text-sm font-mono whitespace-pre-wrap wrap-break-word">{errorMessage}</pre>
            </div>
            <div class="px-6 py-4 bg-gray-50 rounded-b-lg flex justify-end">
                <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700" onclick={closeErrorModal}>
                    返回编辑并定位
                </button>
            </div>
        </div>
    </div>
{/if}
