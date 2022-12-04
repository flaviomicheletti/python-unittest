![image](https://user-images.githubusercontent.com/1257048/203304118-a902976a-72b9-4e7c-bc06-80f73c5afad5.png)

# A short practical guide to testing Python (unittest)

A little guide to help you test your Python code with framework __unittest__.

https://docs.python.org/3/library/unittest.html


# Instalation

__venv:__

    python3 -m venv venv
    . venv/bin/activate

__virtualenv:__

    virtualenv .
    source bin/activate
    pip install --upgrade pip

    deactivate

## Install

In both environments you will need to install it only once.

    pip install mock
    pip install requests
    pip install coverage

## Running

    python -m unittest discover -v
    python -m unittest discover -p 'test_*.py'


## Coverage

    coverage run -m unittest discover
    coverage report -m
    coverage html
