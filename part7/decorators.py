def deco(func):  # decorator replaces function with a different one
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target')


target()  # 'running inner()' will be printed
print(target)  # <function deco.<locals>.inner at 0x102c24d08>
