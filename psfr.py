with open('passwd.txt') as fp:  # context manager
    for temp in fp:
        print(temp, end='')
