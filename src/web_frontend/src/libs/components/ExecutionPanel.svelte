<script>
    let {status} = $props();

    function runOneStep() {

    }

    function runContinue() {

    }

    function runRestart() {

    }
</script>

<div class="flex flex-col h-[500px] md:h-[600px] lg:h-[700px] flex-grow">
    <div class="mt-4">
        <h3 class="font-bold mb-2">Current State:</h3>

        <div class="mt-4 grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div class="bg-blue-100 p-3 rounded">
                <div class="font-semibold">AX: {status.registers.ax}</div>
                <div class="text-gray-600">Register</div>
            </div>
            <div class="bg-blue-100 p-3 rounded">
                <div class="font-semibold">BX: {status.registers.bx}</div>
                <div class="text-gray-600">Register</div>
            </div>
            <div class="bg-blue-100 p-3 rounded">
                <div class="font-semibold">CX: {status.registers.cx}</div>
                <div class="text-gray-600">Register</div>
            </div>
            <div class="bg-blue-100 p-3 rounded">
                <div class="font-semibold">DX: {status.registers.dx}</div>
                <div class="text-gray-600">Register</div>
            </div>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div class="bg-gray-100 p-3 rounded">
                <div class="font-semibold">IP: {status.registers.ip}</div>
                <div class="text-gray-600">Instruction Pointer</div>
            </div>
            <div class="bg-gray-100 p-3 rounded">
                <div class="font-semibold">SP: {status.registers.sp}</div>
                <div class="text-gray-600">Stack Pointer</div>
            </div>
            <div class="bg-gray-100 p-3 rounded">
                <div class="font-semibold">BP: {status.registers.bp}</div>
                <div class="text-gray-600">Base Pointer</div>
            </div>
            <div class="bg-gray-100 p-3 rounded">
                <div class="font-semibold">FLG: {status.registers.flg}</div>
                <div class="text-gray-600">Flag Register</div>
            </div>
        </div>

    </div>

    <div class="mt-4 flex space-x-2">
        <button
                class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
                onclick={() => runOneStep()}
                disabled={status.isRunning||status.halted}
        >
            Run One Step
        </button>
        <button
                class="px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300"
                onclick={() => runContinue()}
                disabled={status.isRunning||status.halted}
        >
            Continue
        </button>
        <button
                class="px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300"
                onclick={() => runRestart()}
        >
            Restart
        </button>
    </div>

    <div class="flex-grow border border-gray-300 rounded-lg p-4 bg-gray-50 overflow-auto font-mono text-sm whitespace-pre-wrap mt-2">
        <textarea class="w-full h-full p-2 font-mono text-sm resize-none focus:outline-none" bind:value={status.output}
                  placeholder="Execution output appears here..."></textarea>
    </div>

</div>