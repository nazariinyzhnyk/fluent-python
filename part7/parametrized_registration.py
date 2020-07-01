registry = set()


def register(active=True):
    def decorate(func):
        print('Running registry (active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=False)
def f1():
    print('Running f1()')


@register()  # need parentheses, as parametrized decorator
def f2():
    print('Running f2()')


def f3():
    print('Running f3()')


if __name__ == '__main__':
    f1()
    f2()
    f3()
    print(registry)  # {<function f2 at 0x102c441e0>}
