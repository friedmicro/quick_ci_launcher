import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Web Configuration Client
 * Handles web browser and program configuration operations
 */
class WebConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch web programs configuration
   * GET /api/config/web/programs
   * @returns {Promise<Object>} Web programs configuration
   */
  async fetchPrograms() {
    const response = await this.client.get("/api/config/web/programs");
    return response.data;
  }

  /**
   * Update web config (programs)
   * POST /api/config/web/config
   * @param {Object} newConfig - New web configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateConfig(newConfig) {
    const response = await this.client.post("/api/config/web/config", {
      new_config: newConfig,
    });
    return response.data;
  }

  /**
   * Fetch web browser configuration
   * GET /api/config/web/browser
   * @returns {Promise<Object>} Web browser configuration
   */
  async fetchBrowser() {
    const response = await this.client.get("/api/config/web/browser");
    return response.data;
  }

  /**
   * Update web browser configuration
   * POST /api/config/web/browser
   * @param {Object} newBrowser - New browser configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateBrowser(newBrowser) {
    const response = await this.client.post("/api/config/web/browser", {
      new_browser: newBrowser,
    });
    return response.data;
  }

  /**
   * Fetch web close_existing configuration
   * GET /api/config/web/close_existing
   * @returns {Promise<Object>} Close existing configuration
   */
  async fetchCloseExisting() {
    const response = await this.client.get("/api/config/web/close_existing");
    return response.data;
  }

  /**
   * Update web close_existing configuration
   * POST /api/config/web/close_existing
   * @param {Object} newCloseExisting - New close existing configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateCloseExisting(newCloseExisting) {
    const response = await this.client.post("/api/config/web/close_existing", {
      new_close_existing: newCloseExisting,
    });
    return response.data;
  }

  /**
   * Fetch web kiosk configuration
   * GET /api/config/web/kiosk
   * @returns {Promise<Object>} Kiosk configuration
   */
  async fetchKiosk() {
    const response = await this.client.get("/api/config/web/kiosk");
    return response.data;
  }

  /**
   * Update web kiosk configuration
   * POST /api/config/web/kiosk
   * @param {Object} newKiosk - New kiosk configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateKiosk(newKiosk) {
    const response = await this.client.post("/api/config/web/kiosk", {
      new_kiosk: newKiosk,
    });
    return response.data;
  }

  /**
   * Fetch web check_ip configuration
   * GET /api/config/web/check_ip
   * @returns {Promise<Object>} Check IP configuration
   */
  async fetchCheckIP() {
    const response = await this.client.get("/api/config/web/check_ip");
    return response.data;
  }

  /**
   * Update web check_ip configuration
   * POST /api/config/web/check_ip
   * @param {Object} newCheckIP - New check IP configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateCheckIP(newCheckIP) {
    const response = await this.client.post("/api/config/web/check_ip", {
      new_check_ip: newCheckIP,
    });
    return response.data;
  }
}

export default WebConfigClient;
