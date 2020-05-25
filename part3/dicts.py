from types import MappingProxyType
from collections import defaultdict, UserDict, Counter

# dicts and sets work with hash table under the hood
# dict=key(hashable), value(any)
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('three', 3), ('one', 1)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a)
print(a == b == c == d == e)

# dict comprehension - from genexp
codes = [('UA', 1),
         ('US', 2),
         ('UK', 3)]

countries = {country: code for country, code in codes}
print(countries)
countries = {code: country.upper() for country, code in countries.items() if code >= 2}
print(countries)

# using defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

print(sorted(d.items()))

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))


class CustomDefaultDict(UserDict):  # better to override UserDict, not builtin dict
    # if add __missing__ method to dict, can get default value
    def __missing__(self, key):
        return 0


a = CustomDefaultDict({"a": 2, "b": 3})
print(a)
print(a['a'])
print(a['miss'])


# Counter example
ct = Counter('ababagalamaga')
print(ct)

ct.update('abracadabra')
print(ct)

print(ct.most_common(3))

# creating an immutable mapping
d = {'a': 5, 'RT': '12'}
print(d)

d['g'] = 12
print(d)

# d = MappingProxyType(d)
# d['g'] = 45
# TypeError: 'mappingproxy' object does not support item assignment
