def open_todos(filepath="todo.txt"):
    """Reads the text file where the to-do tasks are stored"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_arg, filepath="todo.txt"):
    """Writes to-do tasks in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)