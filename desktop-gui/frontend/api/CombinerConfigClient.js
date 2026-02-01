import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Combiner Configuration Client
 * Handles combiner-specific configuration operations including time limits,
 * exceptions, files, and schedules
 */
class CombinerConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Get time limit configuration for a specific config
   * GET /api/config/combiner/time_limit/<config_name>
   * @param {string} configName - Configuration name
   * @returns {Promise<Object>} Time limit configuration
   */
  async getTimeLimit(configName) {
    const response = await this.client.get(
      `/api/config/combiner/time_limit/${configName}`,
    );
    return response.data;
  }

  /**
   * Update time limit configuration for a specific config
   * POST /api/config/combiner/time_limit/<config_name>
   * @param {string} configName - Configuration name
   * @param {boolean} timeLimit - Time limit status
   * @returns {Promise<Object>} Response with success message
   */
  async updateTimeLimit(configName, timeLimit) {
    const response = await this.client.post(
      `/api/config/combiner/time_limit/${configName}`,
      { time_limit: timeLimit },
    );
    return response.data;
  }

  /**
   * Fetch time exceptions configuration for a specific config
   * GET /api/config/combiner/time_exceptions/<config_name>
   * @param {string} configName - Configuration name
   * @returns {Promise<Object>} Time exceptions configuration
   */
  async getTimeExceptions(configName) {
    const response = await this.client.get(
      `/api/config/combiner/time_exceptions/${configName}`,
    );
    return response.data;
  }

  /**
   * Update time exceptions configuration for a specific config
   * POST /api/config/combiner/time_exceptions/<config_name>
   * @param {string} configName - Configuration name
   * @param {Object} exceptions - Time exceptions object
   * @returns {Promise<Object>} Response with success message
   */
  async updateTimeExceptions(configName, exceptions) {
    const response = await this.client.post(
      `/api/config/combiner/time_exceptions/${configName}`,
      { exceptions: exceptions },
    );
    return response.data;
  }

  /**
   * Fetch time files configuration for a specific config
   * GET /api/config/combiner/time_files/<config_name>
   * @param {string} configName - Configuration name
   * @returns {Promise<Object>} Time files configuration
   */
  async getTimeFiles(configName) {
    const response = await this.client.get(
      `/api/config/combiner/time_files/${configName}`,
    );
    return response.data;
  }

  /**
   * Update time files configuration for a specific config
   * POST /api/config/combiner/time_files/<config_name>
   * @param {string} configName - Configuration name
   * @param {Array<Object>} files - Files array
   * @returns {Promise<Object>} Response with success message
   */
  async updateTimeFiles(configName, files) {
    const response = await this.client.post(
      `/api/config/combiner/time_files/${configName}`,
      { files: files },
    );
    return response.data;
  }

  /**
   * Fetch time schedule configuration for a specific config
   * GET /api/config/combiner/time_schedule/<config_name>
   * @param {string} configName - Configuration name
   * @returns {Promise<Object>} Time schedule configuration
   */
  async getTimeSchedule(configName) {
    const response = await this.client.get(
      `/api/config/combiner/time_schedule/${configName}`,
    );
    return response.data;
  }

  /**
   * Update time schedule configuration for a specific config
   * POST /api/config/combiner/time_schedule/<config_name>
   * @param {string} configName - Configuration name
   * @param {Array} schedule - Schedule array
   * @returns {Promise<Object>} Response with success message
   */
  async updateTimeSchedule(configName, schedule) {
    const response = await this.client.post(
      `/api/config/combiner/time_schedule/${configName}`,
      { schedule: schedule },
    );
    return response.data;
  }

  /**
   * Fetch all combiner files configuration
   * GET /api/config/combiner/files
   * @returns {Promise<Object>} Files configuration
   */
  async getFiles() {
    const response = await this.client.get("/api/config/combiner/files");
    return response.data;
  }

  /**
   * Add a new combiner file configuration
   * POST /api/config/combiner/files
   * @param {Object} file - File configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async addFile(file) {
    const response = await this.client.post("/api/config/combiner/files", {
      file: file,
    });
    return response.data;
  }
}

export default CombinerConfigClient;
