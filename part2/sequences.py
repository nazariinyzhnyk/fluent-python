import array
from collections import namedtuple

# list comprehension - for list, generator expression - for other types

symbs = 'Aa@$%'
codes = []
for symb in symbs:
    codes.append(ord(symb))

print(codes)

codes = [ord(symb) for symb in symbs]
print(codes)

# map filtration vs list comprehension
map_filtered = list(filter(lambda c: c > 40, map(ord, symbs)))
print(map_filtered)

map_filtered = [ord(s) for s in symbs if ord(s) > 40]
print(map_filtered)

# cartesian product
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(col, size)for col in colors for size in sizes]
print(tshirts)

tshirts = [(col, size) for size in sizes for col in colors]
print(tshirts)

# generator expressions
print(tuple(ord(symb) for symb in symbs))
print(array.array('I', (ord(symb) for symb in symbs)))

for t in ("%s %s" % (col, size) for col in colors for size in sizes):
    print(t)

# tuple unpacking
coords = (1, 2)
print(coords)

coord_x, coord_y = (1, 2)
print(coord_x)
print(coord_y)

coord_x, coord_y = coords
print(coord_x)
print(coord_y)

for i, _ in [('necessary1', 'not necessary1'), ('necessary2', 'not necessary2')]:
    print(i)

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))  # prefixing with star -> unpack

# variable swap without tmp
a, b = 1, 4
print(a)
print(b)

a, b = b, a
print(a)
print(b)

# items grabber
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, b = range(5)
print(a, body, b)

*head, a, b = range(5)
print(head, a, b)

# nested tuple unpacking
areas = [
    ('NY', 35, (2, 3)),
    ('LA', 21, (4, 5)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat', 'long'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for city, pop, (lat, long) in areas:
    print(fmt.format(city, pop, lat, long))

# named tuples
City = namedtuple('City', 'name country population coords')
tokyo = City('Tokyo', 'JP', 24, (18, 32))
print(tokyo)
print(tokyo.country)
print(tokyo.name)
print(tokyo.coords)
print(City._fields)

delhi_data = ('Delhi', 'IN', 45, (32, 45))
dehli = City._make(delhi_data)
print(dehli)
print(dehli._asdict())
