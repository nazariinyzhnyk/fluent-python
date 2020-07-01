import time
import functools


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(sec):
    time.sleep(sec)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@functools.lru_cache(maxsize=128, typed=False)  # stacked decorators d1(d2(func))
@clock
def fibonacci_cache(n):
    if n < 2:
        return n
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)


if __name__ == '__main__':
    print('=' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('=' * 40, 'Calling snooze(.123)')
    factorial(6)
    print(factorial.__name__)  # clocked
    print(fibonacci(4))  # recursive exploding
    print(fibonacci_cache(4))  # NO recursive exploding - results are cached
