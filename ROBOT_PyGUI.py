import PySimpleGUI as sg
import subprocess

# Define the GUI layout
layout = [
    #[sg.Text("Enter a command to run:"), sg.InputText(key="input")],
    [sg.Text('Choose a command'),sg.DropDown(values=['query','verify', 'help'],key='command')],
    [sg.Text('Select an ontology'),sg.FileBrowse("Browse", key="ontology_browse")],
    [sg.Text('Select a query'),sg.FileBrowse("Browse", key="query_browse")],
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
        if values['command']=='query':
            command='robot query --input ' + values['ontology_browse'] + ' --query ' + values['query_browse']
        #Put in the hard coded inputs and outputs of each robot command (query, verify, filter, etc)
        #command = 'robot ' + values["command"] + '' # + ' ' + values["input"] #Add dropdown menu to this line!!
        elif values['command']=='help':
            command = 'robot help'


        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

# Close the window
window.close()
