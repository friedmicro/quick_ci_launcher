import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Base REST API client for Athena entires not under a domain
 */
class ConfigApiClient {
  constructor() {
    this.instance = createAthenaAPIConnection();
  }

  /**
   * Execute operations (start/stop)
   * @param {string} operation - The operation to execute (start/stop)
   * @param {Object} data - Data containing selected_item
   * @returns {Promise<Object>} Response data
   */
  async execOperation(operation, data) {
    const response = await this.instance.post(`/api/exec/${operation}`, data);
    return response.data;
  }

  /**
   * Get all Athena apps configuration
   * @returns {Promise<Object>} Response containing apps configuration
   */
  async fetchAllApps() {
    const response = await this.get("api/list");
    return response;
  }
}

export default ConfigApiClient;
