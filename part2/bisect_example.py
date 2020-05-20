import bisect

# bisect.bisect - index where to insert element
# bisect.insort - insert element to sequence

haystack = [1, 3, 5, 7, 9]
needles = [2, 0, 6, 7]
bisect_fn = bisect.bisect_right

for needle in needles:
    print("Insertion position: " + str(bisect_fn(haystack, needle)))

print(haystack)


# interesting approach of mapping!
def grade(score, breaks=(60, 70, 80, 90), grades='FDCBA'):
    i = bisect.bisect(breaks, score)
    return grades[i]


print([grade(scr) for scr in [33, 45, 98, 54, 65, 78]])

haystack = [1, 3, 5, 7, 9]
for i in [2, 0, 6, 7]:
    bisect.insort(haystack, i)
    print(haystack)
