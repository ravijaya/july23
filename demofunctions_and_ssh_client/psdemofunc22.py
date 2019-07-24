def compute(*args):
    #print(a + b + c)
    print(args)
    print(sum(args))
    print()

items = [11, 22, 33, 44]
compute(items[0], items[1], items[2])
compute(*items)  # objects content as a argument