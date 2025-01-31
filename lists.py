#list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#change
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist3[1:3] = ["blackcurrant", "watermelon"]
print(thislist3)

#adding
thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")
print(thislist4)

thislist5 = ["apple", "banana", "cherry"]
thislist5.insert(1, "orange")
print(thislist5)

#delete
thislist6 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist6.remove("banana")
print(thislist6)

thislist7 = ["apple", "banana", "cherry"]
thislist7.pop(1)
print(thislist7)

thislist8 = ["apple", "banana", "cherry"]
thislist8.pop()
print(thislist8)

thislist9 = ["apple", "banana", "cherry"]
del thislist9[0]
print(thislist9)

thislist10 = ["apple", "banana", "cherry"]
thislist10.clear()
print(thislist10)

#loop list
thislist11 = ["apple", "banana", "cherry"]
for x in thislist11:
    print(x)

thislist12 = ["apple", "banana", "cherry"]
for i in range(len(thislist12)):
    print(thislist12[i])

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

thislist13 = [100, 50, 65, 82, 23]
thislist13.sort()
print(thislist13)

thislist14 = [100, 50, 65, 82, 23]
thislist14.sort(reverse = True)
print(thislist14)

#copy lists
thislist15 = ["apple", "banana", "cherry"]
mylist = thislist15.copy()
print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)









