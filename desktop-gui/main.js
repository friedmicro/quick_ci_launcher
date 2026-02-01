const { app, BrowserWindow } = require("electron");
const { spawn } = require("child_process");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
  });

  win.loadFile("./frontend/index.html");
};

app.whenReady().then(() => {
  // spawn() Note: Add Athena API here running as detached once we fix config paths
  createWindow();
});
