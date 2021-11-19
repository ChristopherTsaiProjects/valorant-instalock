
# Valorant Instalocker
Instalock script for Valorant agent select.

![](https://github.com/JannisMcMak/valorant-instalock/blob/main/logo/logo180.png?raw=true)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/JannisMcMak/valorant-instalock)



## Installation
Download the [latest release](https://github.com/JannisMcMak/valorant-instalock/releases/latest) and extract the archive. Make sure `config.ini` and the logo folder are in the same directory.

## Usage
Run the executable and press the hotkey (default: `F1`) to lock in agent. You can choose the agent via the system tray icon.

## Config 
The default settings can be adjusted in `config.ini`. Save the file and reload the application to apply changes.

- `Hotkey`
- `Delay` - Delay between mouse clicks/movement (`0.4` seems to be the minimum from my testing)

- `AutoClose` - When enabled, the application will close after first hotkey press to eliminate input lag in-game
- `PullData` - When enabled, coordinate and agent data will be pulled from github

- `DefaultAgent` - Chosen agent by default
- `DisabledAgents` - List of agents that are not yet unlocked in-game (comma-separated)

## Build
Build yourself with [PyInstaller](http://www.pyinstaller.org/).
```
pyinstaller -F --paths=<your_path>\Lib\site-packages --noconsole --icon=logo.ico instalock.py
```