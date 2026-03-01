import function

while True:
    user_action = input("Enter add, edit, delete, show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todos = function.get_todo()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        function.write_todo(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            todos = function.get_todo()
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
            function.write_todo(todos)
        except:
            print("Invalid number!")

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:]) - 1
            todos = function.get_todo()
            todos.pop(number)
            function.write_todo(todos)
        except:
            print("Invalid number!")

    elif user_action.startswith('show'):
        todos = function.get_todo()
        for index, todo in enumerate(todos):
            print(f"{index + 1}- {todo.strip()}")

    elif user_action.startswith('exit'):
        break

print("Good Bye!")