

input_list = ["amuza", "mugisha", "akiri", "tito"]
def exercise1(list_string):
    my_dict={}
    for i in list_string:
        my_dict[i]=len(i)
    return my_dict
    
exercise1(input_list)
print(exercise1(input_list))