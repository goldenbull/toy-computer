import tailwindcss from "@tailwindcss/vite";
import {sveltekit} from "@sveltejs/kit/vite";
import {defineConfig} from "vite";
import path from "path";

export default defineConfig({
    plugins: [tailwindcss(), sveltekit()],
    server: {
        proxy: {
            // Proxy API requests to Python backend during development
            // '/toy-computer/api': {
            '/api': {
                target: 'http://127.0.0.1:22000',
                changeOrigin: true
            }
        }
    }
});
