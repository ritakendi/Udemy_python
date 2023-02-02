import PySimpleGUI as sg

feet_input = sg.Text("Enter feet: ")
input_box1 = sg.Input()

inches_input = sg.Text("Enter inches")
input_box2 = sg.Input()

button = sg.Button("convert")

window = sg.Window("Convertor",
                     layout=[[feet_input, input_box1],
                     [inches_input, input_box2],
                     [button]])

window.read()
window.close()