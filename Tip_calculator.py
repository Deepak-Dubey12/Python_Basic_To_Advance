''' Here we are going to create program to calculate when you are going with friends how much money you need to pay when
equally divide with how much you need to pay tip'''

print("Welcome to the TIP Calculator ! ")
bill = float(input("Enter What was the Total Bill :=  $"))
tip = float(input("Enter How Much Tip You Want To Give 10%, 15% ,or 20% := "))
people=int(input("How many people split this bill payment := "))
tip_as_percent = tip / 100
total_tip_amount =  tip_as_percent * bill
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount=(round(bill_per_person,2))
print(f"Each person should need to pay {final_amount}")

