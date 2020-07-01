# OO approach
class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))


def make_averager():
    # closure
    series = []

    def averager(new_value):
        series.append(new_value)  # series - free variable, could now be reassigned!!!
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))

print(avg.__code__.co_varnames)  # ('new_value', 'total')
print(avg.__code__.co_freevars)  # ('series',)
print(avg.__closure__)  # (<cell at 0x1033fd1c8: list object at 0x1033f4b88>,)
print(avg.__closure__[0].cell_contents)  # [10, 11, 12, 13]


def make_averager():
    total = 0
    count = 0

    def averager(new_value):
        nonlocal total, count  # without nonlocal: UnboundLocalError:local variable 'total' referenced before assignment
        total += new_value
        count += 1
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))
