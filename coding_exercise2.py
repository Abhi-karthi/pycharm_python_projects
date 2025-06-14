ranking = ['John', 'Sen', 'Lisa']
while True:
    a = False
    while a==False:

        try:
            b = float(input("Enter rank: "))
            if b < 3 and b > 0 or b.isdigit():
                a = True
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("please enter a number")
        if b == 1:
            print(ranking[0])
        elif b == 2:
            print(ranking[1])
        elif b == 3:
            print(ranking[2])
