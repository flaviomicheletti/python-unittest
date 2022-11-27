![image](https://user-images.githubusercontent.com/1257048/203304118-a902976a-72b9-4e7c-bc06-80f73c5afad5.png)

# A Brief Guide to Python Testing

A little guide to help you test your Python code.


# Instalation

__venv:__

    python3 -m venv venv
    . venv/bin/activate

__virtualenv:__

    virtualenv .
    source bin/activate
    pip install --upgrade pip
    pip install mock
    deactivate


## Running

    python -m unittest discover -p 'test_*.py'
