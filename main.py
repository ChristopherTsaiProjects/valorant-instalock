import pyautogui
import json
import time
import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

def load_config():
    f = open("config.json")
    config = json.load(f)
    
    return config

config = load_config()

def menu_init():
    app = QApplication(sys.argv)
    trayIcon = QSystemTrayIcon(QIcon("logo/logo.png"), parent=app)
    trayIcon.setToolTip('Instalocker')
    trayIcon.show()

    menu = QMenu()
    menu.addAction('Exit').triggered.connect(app.quit)
    menu2 = menu.addMenu("Choose agent")

    for agent in config["agents"]:
        action = menu2.addAction(agent)
        action.setCheckable(True)

    trayIcon.setContextMenu(menu)
    
    return app


def lock(agent):

    coords = config["coordinates"][config["agents"].index(agent)]
    
    pyautogui.click(coords[0], coords[1])
    time.sleep(config["settings"]["delay"])
    pyautogui.click(config["button"][0], config["button"][1])


if __name__ == "__main__":
    app = menu_init()
    print(app)
    #lock("Yoru")

    sys.exit(app.exec_())


