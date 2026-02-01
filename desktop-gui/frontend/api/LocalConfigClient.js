import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Local Configuration Client
 * Handles local-specific configuration operations
 */
class LocalConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch local configuration
   * GET /api/config/local/local
   * @returns {Promise<Object>} Local configuration
   */
  async fetchLocal() {
    const response = await this.client.get("/api/config/local/local");
    return response.data;
  }

  /**
   * Update local configuration
   * POST /api/config/local/local
   * @param {Object} localConfig - Local configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateLocal(localConfig) {
    const response = await this.client.post("/api/config/local/local", {
      local: localConfig,
    });
    return response.data;
  }
}

export default LocalConfigClient;
