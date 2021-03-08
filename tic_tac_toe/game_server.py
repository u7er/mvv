

def trace(f):
    pass


def max(*args):
    print(f'max{args} = ...')
    ret = -((2**32)-1)
    for x in args:
        ret = ret if x < ret else x
    print(f'max{args} = {ret}')
    return ret

def foo():
    max(-10, -1, -3)

foo()
