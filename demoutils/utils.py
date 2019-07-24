from os import listdir


def ls(path='.'):
    for item in listdir(path):
        print(item)


def power(x, n):
    return x ** n

