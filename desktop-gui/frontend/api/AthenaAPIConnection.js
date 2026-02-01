import axios from "axios";

/**
 * Axios configuration with UUID-based authentication
 * Follows the API authentication system described in AUTH_GUIDE.md
 */

// API Token storage key (used to store the UUID in localStorage)
const API_TOKEN_KEY = "athena_api_token";

/**
 * Get the stored API token from localStorage
 * @returns {string|null} The stored UUID or null if not found
 */
export function getApiToken() {
  try {
    const token = localStorage.getItem(API_TOKEN_KEY);
    return token || null;
  } catch (error) {
    console.error("Failed to read API token from localStorage:", error);
    return null;
  }
}

/**
 * Store an API token in localStorage
 * @param {string} token - The UUID token to store
 */
export function setApiToken(token) {
  try {
    localStorage.setItem(API_TOKEN_KEY, token);
  } catch (error) {
    console.error("Failed to store API token in localStorage:", error);
  }
}

/**
 * Create an axios instance with UUID authentication
 * This instance will automatically include Bearer token in headers
 * @returns {axios.AxiosInstance} Authenticated axios instance
 */
export function createAthenaAPIConnection() {
  const apiToken = getApiToken();

  const instance = axios.create({
    baseURL: config.baseURL,
    headers: {
      "Content-Type": "application/json",
      ...{ Authorization: `Bearer ${apiToken}` },
    },
  });

  // Add response interceptor for handling auth errors
  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      const { status, data } = error.response || {};

      switch (status) {
        case 401:
          alert("API authentication failed (401):", data?.error);
          break;
        case 403:
          alert("API access forbidden (403):", data?.error);
          break;
        default:
          alert("API error:", data?.error);
          break;
      }

      return Promise.reject(error);
    },
  );

  return instance;
}

/**
 * Default authenticated axios configuration
 * Can be used for creating API clients
 * @property {number} timeout - Request timeout in milliseconds
 * @property {string} retryDelay - Delay before retry attempt in milliseconds
 */
export const axiosAuthConfig = {
  timeout: 10000,
  // No retry mechanism by default to avoid infinite loops on 401
};
