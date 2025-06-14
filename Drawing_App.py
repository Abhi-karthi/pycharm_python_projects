import turtle
a = 0
user_amount = 0
user_operation = 0
print("Hello welcome to the drawing app.")
while True:
    a = 0
    user_operation = input("What do you want to do?")
    try:
        user_amount = int(input("What is your amount/color(just type a random integer if your are restarting, pen up, or pen down)? "))
    except ValueError:
        if user_amount != "red" or "orange" or "yellow" or "green" or "blue" or "purple" or "brown" or "white" or "black":
            if user_operation == "color":
                pass
            else:
                a = 1
        else:
            print("Please enter an integer for the amount (unless it is a valid color).")
    if user_operation == "forward":
        turtle.forward(user_amount)
    elif user_operation == "backward":
        turtle.backward(user_amount)
    elif user_operation == "left":
        turtle.left(user_amount)
    elif user_operation == "right":
        turtle.right(user_amount)
    elif user_operation == "color":
        if a == 0:
            turtle.pencolor(user_amount)
        else:
            print("Something went wrong")
    elif user_operation == "restart":
        turtle.clearscreen()
    elif user_operation == "pen up":
        turtle.penup()
    elif user_operation == "pen down":
        turtle.pendown()

    else:
        print("Please type in a valid statement.")