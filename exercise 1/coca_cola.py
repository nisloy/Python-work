accepted_coins=[25,10,5]
entered_coin=int(input("Enter a coin to have your soda"))
amount=0
if entered_coin not in accepted_coins:
     print("You must enter an allowed coin")
amount+=entered_coin

while amount<50:
    enter_another_coin=int(input("Enter a new coin to fit amount"))
    if entered_coin not in accepted_coins:
        print("You must enter an allowed coin")
    else:
        amount+=enter_another_coin
if amount==50:
    print("You have got your soda now ")
while amount>50:
    change=amount-50
    print(f"Your amoiunt have exceede here is your change of {str(change)}")