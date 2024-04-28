import functions as ff
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key="dela")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=ff.get_todos(), key='items',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')


window = sg.Window('My To - Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['items'])
    match event:
        case "Add":
            todos = ff.get_todos()
            new_todos = values['dela'] + "\n"
            todos.append(new_todos)
            ff.write_todos(todos)
            window['items'].update(values=todos)
        case "Edit":
            todo_to_edit = values['items'][0]
            new_todo = values['dela']

            todos = ff.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            ff.write_todos(todos)
            window['items'].update(values=todos)
        case "items":
            window['dela'].update(value=values['items'][0])
        case sg.WIN_CLOSED:
            break


window.close()