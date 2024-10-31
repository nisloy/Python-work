
amount_due=50
total_inserted=0
print("Welcome to coca cola machine")
print("You must inly enter 50, 25, 5 coins")
while total_inserted< amount_due:
    amount=amount_due-total_inserted
    print("Yor Left with this Amount to grab your COCA-COLA",amount)
    coin=int(input("Please enter a allowed coin: "))
    if coin==5  or coin==10 or coin==25:
        total_inserted=total_inserted+coin
    else:
        print("Please enter only allowed coin?")
if total_inserted>50:
    change=total_inserted-amount_due
    print("Your change is ",change)