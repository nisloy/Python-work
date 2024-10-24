my_list=[2,2,1,3,4,5,6,7,8,9,10]
def excise3(list):
    sum_of_odd=0
    sum_of_even=0
    for i in my_list:
        if i%2==0:
            sum_of_even+=i
        else:
            sum_of_odd+=i
    return(sum_of_even,sum_of_odd)
print(excise3(my_list))