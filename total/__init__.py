def read(filename):
    """read a text file and return a list of numbers"""
    with open(filename) as f:
        lines = f.readlines()
        return [float(line.strip()) for line in lines]


def calculate(filename):
    """return the sum of numbers in a text file"""
    numbers = read(filename)
    return sum(numbers)
