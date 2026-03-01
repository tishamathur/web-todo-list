import FreeSimpleGUI as sg
import function
import datetime
sg.theme("bluepurple")

# --------- Get Current Date & Time ---------
now = datetime.datetime.now()
current_time = now.strftime("%d %B %Y  |  %I:%M %p")

# --------- UI Elements ---------
time_label = sg.Text(current_time, key="clock")

label = sg.Text("Enter a todo")
input_box = sg.InputText(key="todo")

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")

list_box = sg.Listbox(
    values=function.get_todo(),
    key="todos",
    enable_events=True,
    size=(45, 10)
)

# --------- Window ---------
window = sg.Window(
    "My Professional Todo App",
    layout=[
        [time_label],
        [label],
        [input_box, add_button],
        [list_box],
        [edit_button, delete_button]
    ],
    font=("Arial", 16)
)

# --------- Event Loop ---------
while True:
    event, values = window.read(timeout=1000)

    # Update clock every second
    now = datetime.datetime.now()
    current_time = now.strftime("%d %B %Y  |  %I:%M %p")
    window["clock"].update(current_time)

    if event == sg.WINDOW_CLOSED:
        break

    # --------- ADD ---------
    if event == "Add":
        todos = function.get_todo()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        function.write_todo(todos)
        window["todos"].update(values=todos)
        window["todo"].update("")

    # --------- EDIT ---------
    if event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = function.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todo(todos)

            window["todos"].update(values=todos)
            window["todo"].update("")
        except IndexError:
            sg.popup("Please select a todo first!")

    # --------- DELETE ---------
    if event == "Delete":
        try:
            todo_to_delete = values["todos"][0]
            todos = function.get_todo()
            todos.remove(todo_to_delete)
            function.write_todo(todos)
            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("Please select a todo first!")

window.close()