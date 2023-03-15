def multiplier(num1, num2):
    start_value = 0     # accumulator
    for _ in range(num2):
        start_value = start_value + num1
    return start_value


def exponentiator(num1, num2):
    start_value = 1
    for _ in range(num2):
        start_value = start_value * multiplier(num1, num2)
    return start_value

def square(num1):
    return multiplier(num1, num1)


def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = multiplier(num1, num2)
    print(result)
    result = exponentiator(num1, num2)
    print(result)
    result = square(num1)
    print(result)

main()

# print(multiplier(4, 7))
# print(exponentiator(4, 7))
# print(square(4))