import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Emulators Configuration Client
 * Handles emulator-specific configuration operations including remapping, selection, and emulator settings
 */
class EmulatorsConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch emulator remapping configuration
   * GET /api/config/emulators/remapping
   * @returns {Promise<Object>} Remapping configuration
   */
  async fetchRemapping() {
    const response = await this.client.get("/api/config/emulators/remapping");
    return response.data;
  }

  /**
   * Update emulator remapping configuration
   * POST /api/config/emulators/remapping
   * @param {Object} remapping - Remapping configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateRemapping(remapping) {
    const response = await this.client.post("/api/config/emulators/remapping", {
      remapping: remapping,
    });
    return response.data;
  }

  /**
   * Fetch selected emulators configuration
   * GET /api/config/emulators/selected
   * @returns {Promise<Object>} Selected emulators configuration
   */
  async fetchSelected() {
    const response = await this.client.get("/api/config/emulators/selected");
    return response.data;
  }

  /**
   * Update selected emulators configuration
   * POST /api/config/emulators/selected
   * @param {Array} selected - Array of selected emulator names
   * @returns {Promise<Object>} Response with success message
   */
  async updateSelected(selected) {
    const response = await this.client.post("/api/config/emulators/selected", {
      selected: selected,
    });
    return response.data;
  }

  /**
   * Fetch all emulators configuration
   * GET /api/config/emulators/emulators
   * @returns {Promise<Object>} All emulators configuration
   */
  async fetchEmulators() {
    const response = await this.client.get("/api/config/emulators/emulators");
    return response.data;
  }

  /**
   * Fetch a specific emulator configuration
   * GET /api/config/emulators/emulator/<emulator_name>
   * @param {string} emulatorName - Emulator name
   * @returns {Promise<Object>} Emulator configuration
   */
  async fetchEmulator(emulatorName) {
    const response = await this.client.get(
      `/api/config/emulators/emulator/${emulatorName}`,
    );
    return response.data;
  }

  /**
   * Update a specific emulator configuration
   * POST /api/config/emulators/emulator/<emulator_name>
   * @param {string} emulatorName - Emulator name
   * @param {Object} emulator - Emulator configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateEmulator(emulatorName, emulator) {
    const response = await this.client.post(
      `/api/config/emulators/emulator/${emulatorName}`,
      { emulator: emulator },
    );
    return response.data;
  }

  /**
   * Add a new emulator configuration
   * POST /api/config/emulators/emulators
   * @param {Object} emulator - Emulator configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async addEmulator(emulator) {
    const response = await this.client.post("/api/config/emulators/emulators", {
      emulator: emulator,
    });
    return response.data;
  }
}

export default EmulatorsConfigClient;
