def demo(*args):
    """variable len argument parameter"""
    print(args)
    # print(type(args))


demo()  # skipped
demo(1)
demo(1, 2, 'iii', 4, 5.5)
