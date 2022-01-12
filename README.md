
# Valorant Instalocker
Instalock script for Valorant agent select.

![](https://github.com/JannisMcMak/valorant-instalock/blob/main/logo/logo180.png?raw=true)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/JannisMcMak/valorant-instalock)



## Installation
Download the [latest release](https://github.com/JannisMcMak/valorant-instalock/releases/latest) and extract the archive. Make sure `config.ini` and the folder `logo` are in the same directory as the executable.

Open the config file and adjust the settings.

## Usage
Run the executable and press the hotkey (default: `F1`) to lock in agent. You can choose the agent via the system tray icon.

If you get a popup saying that Windows Defender protected your PC, just click `More info` and `Run Anyway`.

## Config 
The default settings can be adjusted in `config.ini`. Save the file and reload the application to apply changes.

- `Hotkey`
- `ScreenX, ScreenY` - Your screen resolution
- `DefaultAgent` - Selected agent by default
- `DisabledAgents` - List of agents that are not yet unlocked in-game (comma-separated)

- `Delay` - Delay (in ms) between mouse clicks/movement (`0.4` seems to be the minimum from my testing)

- `AutoClose` - When enabled, the application will close after first hotkey press
- `PullData` - When enabled, coordinate and agent data will be pulled from github

## Build
Build yourself with [PyInstaller](http://www.pyinstaller.org/).
```
pyinstaller -F --paths=<your_path>\Lib\site-packages --noconsole --icon=logo.ico instalock.py
```