FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
        This function is used to retrieve the list of to-dos from a text file called 'todos.txt'.
        The function uses the open() method to open the file_local in read mode and assigns it to the variable file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# def get_todos(filepath=FILEPATH):
#     """
#         This function is used to retrieve the list of to-dos from a text file called 'todos.txt'.
#         The function uses the open() method to open the file_local in read mode and assigns it to the variable file.
#     """
#     with open(filepath, 'r') as file_local:
#         todos_local = [line.strip() for line in file_local.readlines()]
#     return todos_local


# def write_todos(todos_arg, filepath=FILEPATH):
#     """ 
#         write to todos.txt the items entered by user
#     """
#     with open(filepath, 'w') as file:
#         file.writelines(todos_arg)

def write_todos(todos_arg, filepath=FILEPATH):
    '''
         write to todos.txt the items entered by user
    '''
    with open(filepath, 'w') as file:
        file.write('\n'.join(todos_arg))