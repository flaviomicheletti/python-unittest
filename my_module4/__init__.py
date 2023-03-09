# my_module.py
import os

def create_file(filename):
    if os.path.exists(filename):
        return False
    else:
        with open(filename, 'w') as f:
            f.write('Hello, world!')
        return True
