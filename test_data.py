import json
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
config = config["Settings"]

def plot_coords_from_ratios():
    with open('data.json') as json_file:
        data = json.load(json_file)

    sx = int(config["ScreenX"])
    sy = int(config["ScreenY"])
    x = []
    y = []
    for a in data["coordinates"]:
        x.append(int(a[0] * sx))
        y.append(sy-int(a[1] * sy))

    plt.xlim([0, sx])
    plt.ylim([0, sy])

    plt.plot(x, y, 'o', color="red")
    plt.show()

def plot_coords():
    with open('data_absolute.json') as json_file:
        data = json.load(json_file)

    x = []
    y = []
    for a in data["coordinates"]:
        x.append(a[0])
        y.append(1080-a[1])

    plt.xlim([0, 1920])
    plt.ylim([0, 1080])

    plt.plot(x, y, 'o', color="red")
    plt.show()


def convert_absolute_to_ratios():
    with open("data_absolute.json") as f:
        absolute_data = json.load(f)

    for a in absolute_data["coordinates"]:
        a[0] = a[0] / 1920
        a[1] = a[1] / 1080

    absolute_data["button"][0] = absolute_data["button"][0] / 1920
    absolute_data["button"][1] = absolute_data["button"][1] / 1080

    with open("data.json", "w") as f:
        json.dump(absolute_data, f, indent=4)


def convert_ratios_to_4k():
    with open("data.json") as f:
        absolute_data = json.load(f)

    for a in absolute_data["coordinates"]:
        a[0] = int(a[0] * 3840)
        a[1] = int(a[1] * 2160)

    absolute_data["button"][0] = int(absolute_data["button"][0] * 3840)
    absolute_data["button"][1] = int(absolute_data["button"][1] * 2160)

    with open("data_absolute4k.json", "w") as f:
        json.dump(absolute_data, f, indent=4)    



plot_coords_from_ratios()