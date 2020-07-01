import time

DEFAULT_FORMAT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FORMAT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))  # nice!!!!
            return result
        return clocked
    return decorate


if __name__ == '__main__':
    @clock()
    def snooze(sec):
        time.sleep(sec)

    for _ in range(3):
        snooze(.123)

    @clock('{name}: {elapsed:0.8f}s')
    def snooze(sec):
        time.sleep(sec)

    for _ in range(3):
        snooze(.123)
