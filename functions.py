with open("todo.txt", "a") as file:
    pass


def get_todos():
    with open("todo.txt", "r") as file:
        return [item.strip() for item in file.readlines()]


def write_todos(todos):
    with open("todo.txt", "w") as file:
        for item in todos:
            file.write(item + "\n")