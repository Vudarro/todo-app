# "def" creates a custom function (like "input" or "print"). It returns None if return value is not give explicitly
# "def 'function'('parameter')
FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
