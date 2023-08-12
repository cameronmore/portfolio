import PySimpleGUI as sg
import subprocess

# Define the GUI layout
layout = [
    [sg.Text("Enter a command to run:"), sg.InputText(key="input")],
    [sg.Button("Run"), sg.Button("Cancel")],
    [sg.Output(size=(80, 10))]
]

# Create the window
window = sg.Window("ROBOT GUI", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break

    if event == "Run":
        command = values["input"]
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

# Close the window
window.close()
