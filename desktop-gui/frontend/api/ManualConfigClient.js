import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Manual Configuration Client
 * Handles manual configuration override data operations
 */
class ManualConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch manual configuration data
   * GET /api/config/manual/data
   * @returns {Promise<Object>} Manual configuration data
   */
  async fetchData() {
    const response = await this.client.get("/api/config/manual/data");
    return response.data;
  }

  /**
   * Update manual configuration data at specific index
   * POST /api/config/manual/data/<index>
   * @param {number} index - Index to update
   * @param {Object} data - Data to update
   * @returns {Promise<Object>} Response with success message
   */
  async updateAtIndex(index, data) {
    const response = await this.client.post(
      `/api/config/manual/data/${index}`,
      { data: data },
    );
    return response.data;
  }
}

export default ManualConfigClient;
