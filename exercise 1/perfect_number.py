name="amzua"
my_list=[]
for i in range(1000):
    sum_of_factors=0
    for x in range(1,i):
        if i%x==0:
           sum_of_factors+=x
    if sum_of_factors==i:
        # print(i)
        my_list.append(str(i))
print(f"The perfect numbers are : {' , '.join(my_list)}")

    
         