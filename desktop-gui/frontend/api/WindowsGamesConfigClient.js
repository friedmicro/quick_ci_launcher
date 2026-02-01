import { createAthenaAPIConnection } from "./AthenaAPIConnection";

/**
 * Windows Games Configuration Client
 * Handles Windows games configuration operations
 */
class WindowsGamesConfigClient {
  constructor() {
    this.client = createAthenaAPIConnection();
  }

  /**
   * Fetch windows_games exclude configuration
   * GET /api/config/windows_games/exclude
   * @returns {Promise<Object>} Exclude configuration
   */
  async fetchExclude() {
    const response = await this.client.get("/api/config/windows_games/exclude");
    return response.data;
  }

  /**
   * Update windows_games exclude configuration
   * POST /api/config/windows_games/exclude
   * @param {Object} exclude - Exclude configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateExclude(exclude) {
    const response = await this.client.post(
      "/api/config/windows_games/exclude",
      { exclude },
    );
    return response.data;
  }

  /**
   * Fetch open steam direct configuration
   * GET /api/config/windows_games/open_steam_direct
   * @returns {Promise<Object>} Open steam direct configuration
   */
  async fetchOpenSteamDirect() {
    const response = await this.client.get(
      "/api/config/windows_games/open_steam_direct",
    );
    return response.data;
  }

  /**
   * Update open steam direct configuration
   * POST /api/config/windows_games/open_steam_direct
   * @param {Object} openSteamDirect - Open steam direct configuration object
   * @returns {Promise<Object>} Response with success message
   */
  async updateOpenSteamDirect(openSteamDirect) {
    const response = await this.client.post(
      "/api/config/windows_games/open_steam_direct",
      { open_steam_direct: openSteamDirect },
    );
    return response.data;
  }

  /**
   * Fetch steam path configuration
   * GET /api/config/windows_games/steam_path
   * @returns {Promise<Object>} Steam path configuration
   */
  async fetchSteamPath() {
    const response = await this.client.get(
      "/api/config/windows_games/steam_path",
    );
    return response.data;
  }

  /**
   * Update steam path configuration
   * POST /api/config/windows_games/steam_path
   * @param {string} steamPath - Steam path string
   * @returns {Promise<Object>} Response with success message
   */
  async updateSteamPath(steamPath) {
    const response = await this.client.post(
      "/api/config/windows_games/steam_path",
      { steam_path: steamPath },
    );
    return response.data;
  }
}

export default WindowsGamesConfigClient;
