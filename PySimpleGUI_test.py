import PySimpleGUI as sg

label_column = [
    [sg.Text("velocity:    ")],
    [sg.Text("momentum:    ")],
    [sg.Text("time:        ")],
    [sg.Text("mass:        ")],
    [sg.Text("acceleration:")],
    [sg.Text("distance:    ")],
]

input_column = [
    [sg.In(size=(8,1))],
    [sg.In(size=(8,1))],
    [sg.In(size=(8,1))],
    [sg.In(size=(8,1))],
    [sg.In(size=(8,1))],
    [sg.In(size=(8,1))]
]

layout = [
    [
    sg.Column(label_column),
    sg.VSeparator(),
    sg.Column(input_column)
    ],
    [[sg.Button("Ok")]]
]

window = sg.Window("demo", layout)

while True:
    event, values = window.read()
    if event == "Ok" or event == sg.WIN_CLOSED:
        break
window.close()