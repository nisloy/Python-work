salary =9600000
# 15% every month 
# rate =6%
# house=80000000
# 25% of house=saving ===20,000,000
# monthly salary =800,000
house=80000000
monthly_salary=salary//12
# print(monthly_salary)
monthly_deposit=int((15/100)*monthly_salary)
# print(monthly_deposit)
# principal=int((monthly_deposit*12))
# print(principal)
amount=0
principal=120000
for i in range(1,200,1):
    amount= float(principal*(1+(0.06/12)))
    if(amount>=20000000.0):
        print("Time in month is",i)
        break
    principal=amount+120000
print(f"The time in years is {i//12}")    
    
    

    