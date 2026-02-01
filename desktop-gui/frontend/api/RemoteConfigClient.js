import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Remote Configuration Client
 * Handles remote host configuration operations
 */
class RemoteConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch all remote hosts configuration
   * GET /api/config/remote/hosts
   * @returns {Promise<Object>} Remote hosts configuration
   */
  async fetchHosts() {
    const response = await this.client.get("/api/config/remote/hosts");
    return response.data;
  }

  /**
   * Add a new remote host
   * POST /api/config/remote/hosts
   * @param {Object} data - Data containing host_name and host_config
   * @returns {Promise<Object>} Response with success message
   */
  async addHost(data) {
    const response = await this.client.post("/api/config/remote/hosts", data);
    return response.data;
  }

  /**
   * Update an existing remote host
   * POST /api/config/remote/hosts/<host_name>
   * @param {string} hostName - Host name to update
   * @param {Object} hostConfig - Host configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateHost(hostName, hostConfig) {
    const response = await this.client.post(
      `/api/config/remote/hosts/${encodeURIComponent(hostName)}`,
      { host_config: hostConfig },
    );
    return response.data;
  }

  /**
   * Fetch scan options configuration
   * GET /api/config/remote/scan_options
   * @returns {Promise<Object>} Scan options configuration
   */
  async fetchScanOptions() {
    const response = await this.client.get("/api/config/remote/scan_options");
    return response.data;
  }

  /**
   * Update scan options configuration
   * POST /api/config/remote/scan_options
   * @param {Object} scanOptions - Scan options configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateScanOptions(scanOptions) {
    const response = await this.client.post("/api/config/remote/scan_options", {
      scan_options: scanOptions,
    });
    return response.data;
  }

  /**
   * Fetch remotes to load configuration
   * GET /api/config/remote/remotes_to_load
   * @returns {Promise<Object>} Remotes to load configuration
   */
  async fetchRemotesToLoad() {
    const response = await this.client.get(
      "/api/config/remote/remotes_to_load",
    );
    return response.data;
  }

  /**
   * Update remotes to load configuration
   * POST /api/config/remote/remotes_to_load
   * @param {Array} remotesToLoad - Array of remotes to load
   * @returns {Promise<Object>} Response with success message
   */
  async updateRemotesToLoad(remotesToLoad) {
    const response = await this.client.post(
      "/api/config/remote/remotes_to_load",
      { remotes_to_load: remotesToLoad },
    );
    return response.data;
  }

  /**
   * Fetch defaults configuration
   * GET /api/config/remote/defaults
   * @returns {Promise<Object>} Defaults configuration
   */
  async fetchDefaults() {
    const response = await this.client.get("/api/config/remote/defaults");
    return response.data;
  }

  /**
   * Update defaults configuration
   * POST /api/config/remote/defaults
   * @param {Object} defaults - Defaults configuration
   * @returns {Promise<Object>} Response with success message
   */
  async updateDefaults(defaults) {
    const response = await this.client.post("/api/config/remote/defaults", {
      defaults: defaults,
    });
    return response.data;
  }

  /**
   * Fetch prefer_local configuration
   * GET /api/config/remote/prefer_local
   * @returns {Promise<Object>} Prefer local configuration
   */
  async fetchPreferLocal() {
    const response = await this.client.get("/api/config/remote/prefer_local");
    return response.data;
  }

  /**
   * Update prefer_local configuration
   * POST /api/config/remote/prefer_local
   * @param {boolean} preferLocal - Prefer local setting
   * @returns {Promise<Object>} Response with success message
   */
  async updatePreferLocal(preferLocal) {
    const response = await this.client.post("/api/config/remote/prefer_local", {
      prefer_local: preferLocal,
    });
    return response.data;
  }

  /**
   * Fetch prefer_exceptions configuration
   * GET /api/config/remote/prefer_exceptions
   * @returns {Promise<Object>} Prefer exceptions configuration
   */
  async fetchPreferExceptions() {
    const response = await this.client.get(
      "/api/config/remote/prefer_exceptions",
    );
    return response.data;
  }

  /**
   * Update prefer_exceptions configuration
   * POST /api/config/remote/prefer_exceptions
   * @param {Array} preferExceptions - Prefer exceptions array
   * @returns {Promise<Object>} Response with success message
   */
  async updatePreferExceptions(preferExceptions) {
    const response = await this.client.post(
      "/api/config/remote/prefer_exceptions",
      { prefer_exceptions: preferExceptions },
    );
    return response.data;
  }
}

export default RemoteConfigClient;
