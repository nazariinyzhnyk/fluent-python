# implemented with slice object slice(start, stop, step)
l = [1, 2, 3, 4, 5]
print(l[:2])
print(l[2:])
print(l[1:4:2])
print(l[4:1:-2])

# can define slices!
a = '00001111'
zero_slice = slice(0, 4)
one_slice = slice(4, None)

print(a[zero_slice])
print(a[one_slice])

# assigning to slices
l = list(range(10))
print(l)
l[2:5] = (11, 12)  # must be iterable
print(l)
l[2:5] = [13]  # replace 2 elements with 1
print(l)
del l[2:4]
print(l)

# + and *
l = [1, 2, 3]
print(l * 5)
print(3 * 'abcd')

# list of lists - be careful with * -> reference types!
board = [['_'] * 3 for i in range(3)]
board[2][1] = 'X'
print(board)

board = [['_'] * 3] * 3
board[2][1] = 'X'
print(board)

# augmented assignments
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))  # mutable type => changes in place => id not changed

l = (1, 2, 3)
print(id(l))
l *= 2
print(id(l))  # unmutable type => id changed!

# sorting: sorted() (new) and .sort() (in-place)
fruits = ['banana', 'orange', 'apple']
print(sorted(fruits))
print(fruits)
print(id(sorted(fruits)))
print(id(fruits))

fruits.sort()
print(fruits)
