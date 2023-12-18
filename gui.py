import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Topanga")

clock = sg.Text("", key="clock", font=("Helvetica", 12, "bold"))
label = sg.Text("Type in a new to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=18)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True,
                      size=(43, 10))
edit_button = sg.Button("Edit", size=8)
complete_button = sg.Button("Complete", size=8)
exit_button = sg.Button("Exit", size=10)

column1 = sg.Column([[input_box], [list_box]])
column2 = sg.Column([[add_button], [edit_button, complete_button]])

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [column1, column2],
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

