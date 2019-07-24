"""positional argument/ fixed argument function"""
from os import environ


def get_env():
    """print list of env variable with its values """
    for name, value in environ.items():  # iterate a dict for its key, value pair
        print(name, ':', value)


def power(x, n=0):
    """default argument parameter"""
    return x ** n

get_env()
print(power(4, 5))
print(power(4))
