registry = []


def register(func):
    print('Running register (%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('Running f1()')


@register
def f2():
    print('Running f2()')


def f3():
    print('Running f3()')


if __name__ == '__main__':
    print('running main')
    print('registry -> ', registry)  # even before called f1, f2 will be registered
    f1()
    f2()
    f3()
