def custom_append(user_list,number):
    new_list=user_list[:]
    new_list[len(user_list):]=[number]
    return new_list





user_list=[1,2,3,4,5]
number=100
result=custom_append(user_list,number)
print(result)