import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Steam Configuration Client
 * Handles Steam configuration
 */
class SteamConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch steam remapping configuration
   * GET /api/config/steam/remapping
   * @returns {Promise<Object>} Steam remapping configuration
   */
  async fetchRemapping() {
    const response = await this.client.get("/api/config/steam/remapping");
    return response.data;
  }

  /**
   * Update steam remapping configuration
   * POST /api/config/steam/remapping
   * @param {Object} remapping - Remapping configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateRemapping(remapping) {
    const response = await this.client.post("/api/config/steam/remapping", {
      remapping,
    });
    return response.data;
  }

  /**
   * Fetch steam exclude configuration
   * GET /api/config/steam/exclude
   * @returns {Promise<Object>} Steam exclude configuration
   */
  async fetchExclude() {
    const response = await this.client.get("/api/config/steam/exclude");
    return response.data;
  }

  /**
   * Update steam exclude configuration
   * POST /api/config/steam/exclude
   * @param {Object} exclude - Exclude configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateExclude(exclude) {
    const response = await this.client.post("/api/config/steam/exclude", {
      exclude,
    });
    return response.data;
  }

  /**
   * Fetch steam host configuration
   * GET /api/config/steam/host/<host>
   * @param {string} host - Host name
   * @returns {Promise<Object>} Steam host configuration
   */
  async fetchHost(host) {
    const response = await this.client.get(
      `/api/config/steam/host/${encodeURIComponent(host)}`,
    );
    return response.data;
  }

  /**
   * Update steam host configuration
   * POST /api/config/steam/host/<host>
   * @param {string} host - Host name
   * @param {Object} hostConfig - Host configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateHost(host, hostConfig) {
    const response = await this.client.post(
      `/api/config/steam/host/${encodeURIComponent(host)}`,
      { host: hostConfig },
    );
    return response.data;
  }
}

export default SteamConfigClient;
