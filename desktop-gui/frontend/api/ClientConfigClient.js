import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Client Configuration Client
 * Handles client ID and generator configuration operations
 */
class ClientConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch client ID
   * GET /api/config/client/id
   * @returns {Promise<Object>} Client ID
   */
  async fetchId() {
    const response = await this.client.get("/api/config/client/id");
    return response.data;
  }

  /**
   * Update client ID
   * POST /api/config/client/id
   * @param {string} newId - New client identifier
   * @returns {Promise<Object>} Response with success message
   */
  async updateId(newId) {
    const response = await this.client.post("/api/config/client/id", {
      id: newId,
    });
    return response.data;
  }

  /**
   * Fetch generator configuration
   * GET /api/config/client/generator
   * @returns {Promise<Object>} Generator configuration
   */
  async fetchGenerator() {
    const response = await this.client.get("/api/config/client/generator");
    return response.data;
  }

  /**
   * Update generator configuration
   * POST /api/config/client/generator
   * @param {Object} generatorConfig - Generator configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateGenerator(generatorConfig) {
    const response = await this.client.post("/api/config/client/generator", {
      generator: generatorConfig,
    });
    return response.data;
  }
}

export default ClientConfigClient;
