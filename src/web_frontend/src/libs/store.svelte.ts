import {ComputerStatus} from './ComputerStatus.svelte';
import {WebExecutor} from './WebExecutor';

const STORAGE_KEY = 'toyComputer_sourceCode';

// Initialize status with saved code from localStorage
function initializeStatus(): ComputerStatus {
    const status = new ComputerStatus();

    // Only access localStorage in browser
    if (typeof window !== 'undefined') {
        const savedCode = localStorage.getItem(STORAGE_KEY);
        if (savedCode) {
            status.sourceCode = savedCode;
        }
    }

    return status;
}

// Global state
export const globalStatus = initializeStatus();

// Create executor with scroll callback (will be set by ExecutionPanel)
let outputScrollCallback: (() => void) | null = null;

export const globalExecutor = new WebExecutor(globalStatus, () => {
    if (outputScrollCallback) {
        outputScrollCallback();
    }
});

// Allow ExecutionPanel to register its scroll callback
export function setOutputScrollCallback(callback: () => void) {
    outputScrollCallback = callback;
}

// Export storage key for use in components
export { STORAGE_KEY };
