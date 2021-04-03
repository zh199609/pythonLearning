def test(x, *args):
    print(x)
    print(type(args))


test(1, 5, 66, 6)


def test1(**kwargs):
    print(kwargs)


test1(1, 2, 3, 5)
