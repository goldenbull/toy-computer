<script lang="ts">
    import CodeMirror from "svelte-codemirror-editor";
    import type {ComputerStatus} from '../ComputerStatus.svelte.ts';

    let {status = $bindable(), switchTab}: {
        status: ComputerStatus,
        switchTab: (tab: string) => void
    } = $props();

    const loadSourceCode = () => {
        // TODO: load from disk file
    };

    async function compileCode() {
        // Compile the source code by calling the backend API
        try {
            const response = await fetch('/api/compile', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    sourceCode: status.sourceCode
                })
            });

            const result = await response.json();

            if (!result.success) {
                // Compilation error
                status.output += `Compilation Error: ${result.error}\n`;
                return;
            }

            // Load the compiled operations
            status.loadCompiledCode(result.operations, result.labels);

            // Switch to execution panel
            switchTab('execution');

            // TODO: Start execution
            console.log('Compiled successfully:', result);
            console.log('Operations:', status.operations);

        } catch (error) {
            status.output += `Error: ${error}\n`;
        }
    }

</script>

<div class="flex flex-col h-[500px] md:h-[600px] lg:h-[700px] flex-grow">
    <div class="flex-grow border border-gray-300 rounded-lg overflow-hidden relative">
        <!--        <textarea-->
        <!--                bind:value={status.sourceCode}-->
        <!--                class="w-full h-full p-4 font-mono text-sm resize-none focus:outline-none absolute inset-0"-->
        <!--                placeholder="Enter your assembly code here..."-->
        <!--                spellcheck="false"-->
        <!--        ></textarea>-->
        <CodeMirror bind:value={status.sourceCode}
                    class="w-full h-full p-4 font-mono text-sm resize-none focus:outline-none absolute inset-0"
                    placeholder="Enter your assembly code here..."
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