# def foo(param1, param2):
#     return param1 + param2

# def bar(param1 = 4, param2 = 3): # default values, named params
    # don't set parameter to a list
#     return param1 + param2 # ends the function

# # foo(1) # error
# foo(1, 2)
# # foo(1, 2, 3) #error
# # param1 # error
# bar(1)
# bar()
# bar(1, 3)
# result = bar(param2=1, param1=2)

# # # def max(a=0, b=0):
# # #     if a > b:
# # #         return a
# # #     else:
# # #         return b


# def percentage_to_letter(percent):
#     let = "A"
#     if 80 <= percent < 90:
#         let = "B"
#     elif 70 <= percent < 80:
#         let = "c"
#     elif 60 <= percent < 70:
#         let = "D"
#     elif < 60:
#         let + "F"
#     return let

# def is_passing(letter): # boolean function, in cpnvention
#         if letter.lower() in "abs"

# def percentage_to_letter(percent=99):
#     """
#     This is a function that returns a letter grade based on a percentage
#     args: percent (int)
#     return: letter(Str)
#     """


# def main(): # driver code. Historically called main
#     grades = [90, 80, 70, 60, 50]
#     for grade in grades:
#         letter = percentage_to_letter(grade)
#         if is_passing(letter):
#             print("You passed!")
#         else:
#             print("Someone messed up you grades!")
#     return main
# main()

# programming pattern

# for - programming pattern
# accumulator pattern

# result = 0
# for i in range(10):
#     result - result + i

# print(result)

# accumulator = start_value
# for i in list: 
#   accumulator = accumulator <op> i

def remove_vowels(string):
    vowels = "aeiou"
    vowels += vowels.upper()
    result = ""
    for ch in string:
        if ch not in vowels:
            result = result + ch
    return result

def main():
    mystring = "Hello World"
    print(remove_vowels(mystring))
    print(remove_vowels)
main()