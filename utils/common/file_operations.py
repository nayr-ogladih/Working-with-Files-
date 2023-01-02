from utils.find import NotFoundError


def save_to_file(content, filename): #importing our first library
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read() # 'Rolf\nCharlie\nAnna


print(__name__)