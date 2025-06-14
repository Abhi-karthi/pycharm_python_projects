def calculating_unit(number_one, operation, number_two):
    # function requires integer inputs for number_one and number_two. Operation must be a string.  square root does not require number_two
    if operation == "+":
        return number_one + number_two
    if operation == "-":
        return number_one - number_two
    if operation == "x":
        return number_one * number_two
    if operation == "/":
        return number_one / number_two
    if operation == "√":
        import math
        return math.sqrt(number_one)
    if operation == "^":
        return number_one**number_two


def remove_char_in_string(char, string):
    string_list = list(string)
    pop_list = []
    nums_popped = 0

    for index, value in enumerate(string_list):
        if value == f"{char}":
            pop_list.append(index)

    for i in pop_list:
        string_list.pop(i - nums_popped)
        nums_popped += 1

    final_string = ""

    for i in string_list:
        final_string += i

    return final_string


def binary_search(integer, array):
    lowest = 0
    highest = len(array) - 1
    while array[int((lowest + highest)/2) - 1] != integer:
        if array[int((lowest + highest)/2) - 1] < integer:
            lowest = int((lowest+highest)/2)
        elif array[int((lowest+highest)/2) - 1] < integer:
            highest = int((lowest+highest)/2)

        # print(lowest, highest)

    return int((lowest + highest)/2 - 1)

# print(binary_search(42, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 20, 42, 61, 104]))

