# != : not equal to
# break: ends a loop
# exit(): ends program


# for _ in range(10):
#     for _ in range(10):
#         exit()
#     print(_)

# for num in range(10):
#     print(num)
#     num = num + 5
#     print(num)

# mylist = ['a', 'b', 'c']
# for num in mylist: #num = mylist[n]
#     print(num)
#     num = num + 5
#     print(num)

## ITERATION - looping over something inside an object
# iterable - you can loop over it

# mystr = "hello"
# # string is a fancy, iterable list or characters
# mynums = [1, 2, 3, 4, 5]

# for ch in mystr:
#     print(ch)

# for num in mynums:
#     print(num)

# # anything iterable can be 'indexed' into
# print(mystr[0], mystr[1], mystr[2], mystr[3], mystr[4])

# mynums[0] = 5
# print(mynums)


# #mystr[0] = "J"  ---- can't do this

# # mutable = changeable
# # immutable = can't be changed once created

# num = 5

# mystr = "hello" # immutable
# myotherstring = "hello"

# mynums = [1, 2, 3, 4, 5]
# myothernums= [1, 2, 3, 4, 5]

# if mystr == myotherstring:
#     print("They are the same")

# if mynums == myothernums:
#     print("They are the same")

# if mystr is myotherstring:
#     print("They are the same")

# if mynums is myothernums:
#     print("mynums are the same")






## substring
# mystr = "hello"
# print(mystr[0])
# print(mystr[1:4])
# # : one to the other

# # mystr = mystr[1:5]
# print(mystr.lower(), mystr.upper(), mystr.capitalize(), mystr)

# # iterable objects are not always mutable- can loop through the object, but not always change the object

# # slicing with mutable objects
# mynums = [1, 2, 3, 4, 5]

# # mynums[2:2] = [2.5, 2.6]
# # print(mynums)

# # mynums[3] = [2.5, 2.6]
# # for i in mynums:
# #     print(i)

# # mynums[2:4] = [2.5, 2.6]
# # # overwrote values 2 to 4
# # print(mynums)



# for i in mynums:
#     mynums[i-1] = i * 2
# print(mynums)

# for i in range(len(mynums)):
#     mynums[i] = mynums[i] * 2
# print(mynums)

# # index = 0
# for i, v in enumerate(mynums):
#     # i - index location in list
#     # v - value at the index location
#     print(i, v)
#     mynums[i] = i * 2
#     # index += 1
# print(mynums)

# index = 0
# for v in mynums:
#     mynums[i] = v * 2
#     index += 1
# print(mynums)



# lists are slow

## tuple - immutable list (has parenthesis)
mynums = (1, 4, 6, 54, 3245543, 7) #immutable

# mynums[2] = 2.5
# can't assign to it

x = 5
y = 6

(x, y) = (y, x)

## basic swap algorithm
# temp = x
# x = y
# y = temp

num = [5] * 3
print(num)


#ambiguous:
num = (5) * 3
print(num)

#single element tuples MUST have a trailing comma
num = (5,) * 3
print(num)



mynums = [1, 4, 6, 54, 3245543, 7]
print(list(enumerate(mynums)))

(x, y) = (5,6)
for i, v in enumerate(mynums):
    print(i, v)

contacts = [
    ["bill", "867-5309"],
    ["jane", "555-1212"],
]

# name = input("enter a name: ")

# # worst case scenario
# # looping n times, where n is the number
# for contact in contacts:
#     if contact[0] == name:
#         print(contact[1])
#         break

# relationship index => value

# nums = [0:5, 1:8, 2:1, 3:123456789, 4:5]

# # NOT VALID PYTHON
# contact = [
#     "bill": "867-5309",
#     "jane": "555-1212",
# ]

# print(contact[name])

# dictionary
contact = {
    "bill": "867-5309",
    "jane": "555-1212",
}

print(contact["jane"])
# print(contact["joe"]) # ERROR

# list[index] = value
# dictionary[key] = value
# key/value pairs
# keys must be unique
# keys must be immutable

contact["joe"] = "555-1213"
print(contact)
contact["joe"] = "555-1214"
print(contact)

contact["joe"] = ["555-1214", "555-1213"]
print(contact)


for c in contact:
    print(c)
    print(contact[c])

#items() - enumerate for dictionaries
for key, value in contact.items():
    print(key)
    print(contact[value])

for key in contact.keys():
    print(key)

for val in contact.value():
    print(val)

# print(contact["juan"])

# get() - only for reading

print(contact.get("juan"))

if contact.get("juan"):
    print(contact["juan"])


## data structures for Python
# strings
# lists
# typles
# dictionaries
