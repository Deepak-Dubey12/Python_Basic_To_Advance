# Here I am going to use conditional if and else operator to check that the value of your height are you eligible to go in roller coster

print("Welcome to the Roller Coaster ride : = ")
height = int(input("What is your height in cm :=  "))

if height >= 120:
    print("You are eligible for roller coster ride")
    age=int(input("What is your age := "))
    if age <= 12:
        bill = 5
        print("You need to pay only $5")
    elif age <= 18:
        bill = 7
        print("You need to pay only $7")
    else:
        bill = 12
        print("you need to pay $12")
    want_photoes = input("Do You Want to Take Photoes In Your Roller Coster Ride For Yes say Y For No say N")
    if want_photoes == "Y":
        bill += 3

    print(f"You Just want to pay Normal bill amount {bill} ")
else:
    print("Sorry you have to grow taller before you can ride")
