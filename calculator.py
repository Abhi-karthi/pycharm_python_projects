empty = 0
import processing_units
while True:
    a = 0
    print("Your valid operations are + for addition, - for subtraction, x for multiplication, / for division, ^ for powers, and √ for square root (option + v).")
    try:
        first = int(input("first number:"))
        operation = input("operation:")
        if operation != "√":
            second = int(input("second number:"))
    except ValueError:
        print("Please enter integers.")
        a = 1
    if operation != "+" or operation != "-" or operation != "x" or operation != "/" or operation != "^" or operation != "√":
        a = 1
        print("Please enter one of the operations listed below.")
    if a == 0:
        if operation == "√":
            print(processing_units.calculating_unit(first, operation, empty))
        else:
            print(processing_units.calculating_unit(first, operation, second))
