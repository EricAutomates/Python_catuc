# -------------------------------
# 3-8 Seeing the World
# -------------------------------

'''
3-8 Seeing the World
'''
places = ["Yaoundé", "Douala", "Bamenda", "Limbe", "Garoua"]

'''
Original order
'''
print("Original list:")
print(places)

'''
Alphabetical order with sorted()
'''
print("\nAlphabetical:")
print(sorted(places))

'''
Still original
'''
print("\nStill original:")
print(places)

'''
Reverse alphabetical with sorted()
'''
print("\nReverse alphabetical:")
print(sorted(places, reverse=True))

'''
Still original again
'''
print("\nStill original again:")
print(places)

'''
reverse()
'''
places.reverse()
print("\nAfter reverse():")
print(places)

places.reverse()
print("\nAfter reverse() again (back to original):")
print(places)

'''
sort()
'''
places.sort()
print("\nAfter sort() alphabetical:")
print(places)

places.sort(reverse=True)
print("\nAfter sort() reverse alphabetical:")
print(places)


# -------------------------------
# 3-9 Dinner Guests
# -------------------------------

'''
3-9 Dinner Guests
'''
guests = ["maya", "albert", "eric", "epstien"]
print("\nNumber of dinner guests:", len(guests))


# -------------------------------
# 3-10 Every Function
# -------------------------------

'''
3-10 Every Function
'''
rivers = ["Nile", "Amazon", "Yangtze", "Mississippi", "Danube"]

'''
Original rivers list
'''
print("\nOriginal rivers list:")
print(rivers)

'''
Using append()
'''
rivers.append("Ganges")

'''
Using insert()
'''
rivers.insert(2, "Thames")

'''
Using sorted() without changing list
'''
print("\nAlphabetical (using sorted):")
print(sorted(rivers))

'''
Using reverse()
'''
rivers.reverse()
print("\nAfter reverse():")
print(rivers)

'''
Using sort()
'''
rivers.sort()
print("\nAfter sort():")
print(rivers)

'''
Using pop()
'''
popped = rivers.pop()
print("\nPopped river:", popped)

'''
Using remove()
'''
rivers.remove("Nile")

print("\nFinal rivers list:")
print(rivers)
