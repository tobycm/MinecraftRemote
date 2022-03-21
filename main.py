import json
import PySimpleGUI as sg
import subprocess

with open("config.json", "r") as f:
    config = json.load(f)

process = subprocess.Popen("java -Xms3G -Xmx3G -jar paper-1.16.5-794.jar nogui", stdout=subprocess.PIPE, stdin=subprocess.PIPE, cwd = "D:\\RandomStuff\\MinecraftServer1.16.5\\")

sg.theme('DarkAmber')   # Add a touch of color

output = ""

# All the stuff inside your window.
layout = [  [sg.Text("Minecraft Server Controller")],
            [sg.Text("Command: "), sg.InputText()],
            [sg.Button('Run Command'), sg.Button('Exit')],
            [sg.Multiline("", size=(45,5), autoscroll=True, key='output')]
            ]

# Create the Window
window = sg.Window('Minecraft Server Controller', layout, finalize=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:

    # Read console output
    line = process.stdout.readline()
    if line.decode("utf-8") != '':
        print(line.decode("utf-8"))

    # Read the Window's "values"
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks exit
        break

window.close()

