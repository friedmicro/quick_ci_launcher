import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Android Configuration Client
 * Handles Android-specific configuration operations
 */
class AndroidConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Load Android apps configuration
   * GET /api/config/android/load_apps
   * @returns {Promise<Object>} Apps configuration
   */
  async loadApps() {
    const response = await this.client.get("/api/config/android/load_apps");
    return response.data;
  }

  /**
   * Update Android configuration
   * POST /api/config/android/config
   * @param {Object} apps - Apps configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateConfig(apps) {
    const response = await this.client.post("/api/config/android/config", {
      config: apps,
    });
    return response.data;
  }
}

export default AndroidConfigClient;
