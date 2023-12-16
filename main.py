# importing elements from other .py files
# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    # "str.strip()" removes spaces
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # "str[x:y]" takes only specified part of string - from character with index x to a character right before
        # index y
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1} -- {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input(f"Enter a to-do to replace '{todos[number]}': ")
            # "string + "\n"" to add a break line in save file for better readability later
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
            print("Here are edited to-dos:", todos)
        # if in "try" section Error (actually Exception, since only SyntaxError is a true error) occurs, except catches
        # that particular error and runs code specified
        except ValueError:
            print("Your command is not recognized, try using a number of a to-do after 'edit'")
            # "continue" continues the loop from beginning - opposite of "break"
            continue
        except IndexError:
            print(f"Selected to-do doesn't exist. There are only " + str(len(todos)) + " to-dos to edit.")
            continue

    elif user_action.startswith("complete"):
        number = int(user_action[9:])
        try:
            todos = functions.get_todos()

            index = number - 1
            todo_remove = todos[index].strip("\n")
            # "list.pop()" removes an item from list and then prints it out
            todos.pop(index)

            functions.write_todos(todos)
            print(f"'{todo_remove}' has been completed")
            print("Here are to-dos yet to be completed:", todos)

        except ValueError:
            print("Your command is not recognized, try using a number of a to-do after 'complete'")
            continue
        except IndexError:
            print(f"Selected to-do doesn't exist. There are only " + str(len(todos)) + " to-dos to complete.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not recognized.")

print("Bye.")
