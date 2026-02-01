import { createAuthenticatedAxiosInstance } from "./AthenaAPIConnection";

/**
 * Athena Configuration Client
 * Handles Athena client and daemon configuration operations
 */
class AthenaConfigClient {
  constructor() {
    this.client = createAuthenticatedAxiosInstance();
  }

  /**
   * Fetch Athena configuration
   * GET /api/config/athena/config
   * @returns {Promise<Object>} Athena configuration object
   */
  async fetchConfig() {
    const response = await this.client.get("/api/config/athena/config");
    return response.data;
  }
}

export default AthenaConfigClient;
