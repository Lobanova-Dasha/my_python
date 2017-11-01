#! python3
# calc.py

def add(x, y):
    """Add Function"""
    return x + y


def substract(x, y):
    """Sumstract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def devide(x, y):
    """Devide Function"""
    if y == 0:
        raise ValueError('Can njt divide by zero!')
    return x / y
                 