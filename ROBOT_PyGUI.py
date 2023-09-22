import PySimpleGUI as sg
import subprocess

#sg.theme('DarkGrey5')

sg.popup_ok('Welcome to SimpleROBOT! Here, you can run simple SPARQL SELECT queries, SPARQL files with multiple queries to quality control an ontology, or \'help\' to see everything ROBOT has to offer (when used at the command line)',title='Welcome!')


# Define the GUI layout
layout = [
    [sg.Text('Choose a command'),sg.DropDown(values=['query','verify', 'help'],key='command')],
    [sg.Text('Select an ontology'),sg.FileBrowse("Browse", key="ontology_browse")],
    [sg.Text('Select a query'),sg.FileBrowse("Browse", key="query_browse")],
    [sg.Text('Select a place to store results'),sg.FileBrowse("Browse", key="result_loc")],
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
            command='robot query --input ' + values['ontology_browse'] + ' --query  ' + values['query_browse'] + '  ' + values['results_loc']
            command = command.replace('/','\\')
        elif values['command']=='help':
            command = 'robot help'
        elif values['command']=='verify':
            command='robot verify --input '+ values['ontology_browse'] + ' --queries ' + values['query_browse'] + values['results_loc']
        #Hard code more robot commands here


        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")

# Close the window
window.close()
