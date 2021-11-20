from PyQt5.QtCore import QCoreApplication, QObject, QThread, pyqtSignal, QProcess
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QActionGroup
from PyQt5.QtGui import QIcon
import sys
import json
from pynput import keyboard
import pyautogui
import configparser
import requests

json_data = '{"agents":["Astra","Breach","Brimstone","Chamber","Cypher","Jett","KAY\/O","Killjoy","Omen","Phoenix","Raze","Reyna","Sage","Skye","Sova","Viper","Yoru"],"coordinates":[[0.3255208333333333,0.8601851851851852],[0.3692708333333333,0.8601851851851852],[0.41302083333333334,0.8601851851851852],[0.45677083333333335,0.8601851851851852],[0.5005208333333333,0.8601851851851852],[0.5442708333333334,0.8601851851851852],[0.5880208333333333,0.8601851851851852],[0.6317708333333333,0.8601851851851852],[0.6755208333333333,0.8601851851851852],[0.3255208333333333,0.937962962962963],[0.3692708333333333,0.937962962962963],[0.41302083333333334,0.937962962962963],[0.45677083333333335,0.937962962962963],[0.5005208333333333,0.937962962962963],[0.5442708333333334,0.937962962962963],[0.5880208333333333,0.937962962962963],[0.6317708333333333,0.937962962962963]],"button":[0.5,0.7481481481481481]}'

def load_data():
    config = configparser.ConfigParser()
    config.read("config.ini")
    config = config["Settings"]

    if config["PullData"] == "no":
        data = json.loads(json_data)
    else:
        data = requests.get("https://raw.githubusercontent.com/JannisMcMak/valorant-instalock/main/data.json").json()
    
    return data, config


global data, config
data, config = load_data()

app = QApplication(sys.argv)


class Instalocker(QObject):
    finished = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True
        
        self.agents = self.load_agent_list()
        self.choice = config["DefaultAgent"]

    def on_press(self, key):
        try:
            if str(key).split(".")[1] == config["Hotkey"].lower():
                self.lock_in()
                if config["AutoClose"] == "yes":
                    self.finished.emit()
                    self.stop()

        except:
            return


    def listen(self):            
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def load_agent_list(self):
        agents = data["agents"]
        for agent in agents:
            if agent in config["DisabledAgents"].split(", "):
                agents.remove(agent)   
        return agents

    def lock_in(self):
        coords = data["coordinates"][self.agents.index(self.choice)]

        sx = int(config["ScreenX"])
        sy = int(config["ScreenY"])

        pyautogui.moveTo(coords[0] * sx, coords[1] * sy)
        pyautogui.click()
        pyautogui.click()
        QThread.msleep(int(float(config["Delay"]) * 100))
        pyautogui.moveTo(int(data["button"][0] * sx), int(data["button"][1] * sy))
        pyautogui.click()
        pyautogui.click()


    def stop(self):
        self.continue_run = False


class App(QSystemTrayIcon):
    stop_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(App, self).__init__(QIcon("logo/logo.png"), parent)


        self.setToolTip("Instalocker")
        self.show()


        menu = QMenu()
        menu2 = menu.addMenu("Choose agent")

        agent_group = QActionGroup(menu2)
        
        for agent in data["agents"]:
            action = QAction(agent, menu, checkable=True, checked=agent==config["DefaultAgent"])
            
            action.setEnabled(agent not in config["DisabledAgents"].split(", "))
            menu2.addAction(action)
            agent_group.addAction(action)

        agent_group.setExclusive(True)
        agent_group.triggered.connect(self.on_choice)
        
        menu.addAction('Reload').triggered.connect(self.on_reload)
        menu.addAction('Exit').triggered.connect(self.stop)

        self.setContextMenu(menu)


        self.thread = QThread()
        self.worker = Instalocker()
        self.stop_signal.connect(self.worker.stop)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.listen)
        self.worker.finished.connect(self.stop)

    
    def on_choice(self, action):
        self.worker.choice = action.text()

    def on_reload(self, action):
        QCoreApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)

    def stop(self, action):
        self.thread.quit()
        self.worker.stop()
        self.worker.deleteLater()
        self.thread.deleteLater()
        app.quit()


def main():
    w = App()

    w.thread.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    

