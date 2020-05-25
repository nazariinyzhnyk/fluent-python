# set can only contain hashable objects. unordered
l = ['spam', 'set', 'egg', 'spam', 'egg', 'set']
print(l)
print(list(set(l)))

search_que = {'egg', 'spam', 'lol'}
found = search_que & set(l)  # very fast searching
print(found)
print(search_que.intersection(l))  # no need even to cast l to list

print(frozenset(range(10)))  # immutable set (hashable)

# set comprehension
a = 'aaahhhttt'
s = {i for i in a}
print(s)
