import functions
import PySimpleGUI as sg
import time

sg.theme("Topanga")

clock = sg.Text("", key="clock", font=("Helvetica", 12, "bold"))
label = sg.Text("Type in a new to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=20)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True,
                      size=(43, 20))
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10)


window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 12))
while True:
    event, values = window.read(timeout=20)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)

            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()

                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)

            except IndexError:
                sg.popup("Please select a to-do to edit", font=("Helvetica", 12))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()

                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a to-do to complete", font=("Helvetica", 12))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break


window.close()

