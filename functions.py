filepath_p = 'todoo.txt'


def get_todos(filepath=filepath_p):
    with open(filepath_p, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=filepath_p):
    with open(filepath, "w") as file_loc:
        file_loc.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
