# Here I am going to create an pizza delivery Option. Also we have section option in pizza S ,M, and L
print("Welcome to Python Pizza Deliveries!")
size = input("What size Pizza do you want? S ,M or L : =  ")
if size == "S":
    bill = 15
    print("You need to pay $15")
elif size == "M":
    bill = 20
    print("You need to pay $20")
elif size == "L":
    bill = 25
    print("You need to pay $25")
else:
    print("You print the wrong input")
peporoni = input("Do you want to add peporoni in your Pizza Say Y or N : = ")
if peporoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
    cheese =input("Do you want to add extra Cheese in your Pizza say Y or N : = ")
    if cheese == "Y":
        bill+=1
print(f"The total bill of pizza{bill}")

