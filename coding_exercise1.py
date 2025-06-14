while True:
    a = False
    while a==False:

        try:
            dollars = float(input("Amount in dollars: "))
            a = True
        except ValueError:
            print("please enter a number")
    print("The amount of euros is:")
    print(round(float(dollars*.95), 2))