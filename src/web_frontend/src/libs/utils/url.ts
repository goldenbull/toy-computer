/**
 * Get the base URL from environment configuration
 * Returns the base URL with a trailing slash
 */
export function getBaseUrl(): string {
    const baseUrl = import.meta.env.BASE_URL || '/';
    // Ensure baseUrl ends with /
    return baseUrl.endsWith('/') ? baseUrl : baseUrl + '/';
}

/**
 * Build an API URL with the base URL
 * @param apiPath - The API path (e.g., 'api/compile')
 * @returns The full API URL
 */
export function buildApiUrl(apiPath: string): string {
    const baseUrl = getBaseUrl();
    // Remove leading slash from apiPath if present
    const normalizedPath = apiPath.startsWith('/') ? apiPath.slice(1) : apiPath;
    return `${baseUrl}${normalizedPath}`;
}

/**
 * Build an absolute path with the base URL
 * @param path - The relative path (e.g., 'manual', '/manual')
 * @returns The full path with base URL
 */
export function buildPath(path: string): string {
    const baseUrl = getBaseUrl();
    // Remove leading slash from path if present
    const normalizedPath = path.startsWith('/') ? path.slice(1) : path;
    return `${baseUrl}${normalizedPath}`;
}
