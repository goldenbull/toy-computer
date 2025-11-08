<script>
    let {status, runCode} = $props();

    const loadSourceCode = () => {
        // TODO: load from disk file
    };
</script>

<div class="flex flex-col h-[500px] md:h-[600px] lg:h-[700px] flex-grow">
    <div class="flex-grow border border-gray-300 rounded-lg overflow-hidden relative">
        <textarea
                bind:value={status.sourceCode}
                class="w-full h-full p-4 font-mono text-sm resize-none focus:outline-none absolute inset-0"
                placeholder="Enter your assembly code here..."
                spellcheck="false"
        ></textarea>
    </div>

    <div class="mt-4 flex space-x-2">
        <button
                class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
                onclick={()=>runCode(false)}
                disabled={status.isRunning}
        >
            {status.isRunning ? 'Running...' : 'Run'}
        </button>
        <button
                class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
                onclick={()=>runCode(true)}
                disabled={status.isRunning}
        >
            Run in Step Mode
        </button>
        <button
                class="px-4 py-2 bg-gray-600 text-white rounded hover:bg-gray-700"
                onclick={loadSourceCode}
        >
            Load Source Code
        </button>
    </div>
</div>