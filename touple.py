#tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# tuple1 = ("abc", 34, True, 40, "male")

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

#access tuples
thistuple2 = ("apple", "banana", "cherry")
print(thistuple2[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

#update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

#unpack tuples
fruits2 = ("apple", "banana", "cherry")

(green, yellow, red) = fruits2

print(green)
print(yellow)
print(red)

#loop tuple
thistuple3 = ("apple", "banana", "cherry")
for x in thistuple3:
    print(x)

thistuple4 = ("apple", "banana", "cherry")
for i in range(len(thistuple4)):
    print(thistuple4[i])

#join
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


