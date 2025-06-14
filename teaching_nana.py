while True:
    a = False
    while a==False:

        try:
            year_of_birth = int(input("Your year of birth: "))
            a = True
        except ValueError:
            print("please enter a number")
    age = 2023 - year_of_birth
    print(age)