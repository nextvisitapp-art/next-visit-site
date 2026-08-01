// Remotion config for the Next Visit reel templates.
// On the Claude Code cloud container there is a preinstalled Chromium at
// /opt/pw-browsers/chromium - use it so renders never download a browser.
// On any other machine (Charlie's Mac) Remotion falls back to its own
// managed headless browser.
const fs = require('fs');
const { Config } = require('@remotion/cli/config');

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);

// The plain /opt/pw-browsers/chromium binary has old-headless removed, which
// Remotion's renderer still targets - the headless_shell build next to it is
// the standalone old-headless implementation and is what Remotion expects.
const containerHeadlessShell =
  '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
if (fs.existsSync(containerHeadlessShell)) {
  Config.setBrowserExecutable(containerHeadlessShell);
}
