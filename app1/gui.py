import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme('Black')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                        enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit")

window = sg.Window('My Todo App', 
                    layout=[[clock],
                        [label], 
                        [input_box, add_button], 
                        [list_box,edit_button, complete_button],
                        [exit_button]], 
                    font=("Helvetica", 20))
while True:
    event, values= window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    

    if add_button :
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif edit_button:
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos =functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif 'todos':
        window['todo'].update(value=values['todos'])

    elif complete_button in event:
        todo_to_complete = values['todos'][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')

    elif event.has_exit_button:
        break

    
    
    # elif sg.WIN_CLOSED:
    #     break

window.close()