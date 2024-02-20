def custom_remove(user_list,number):
    new_list=user_list[:]
    digit_to_remove=user_list.index(number)
    new_list=new_list[:digit_to_remove]+new_list[digit_to_remove+1:]
    return new_list





user_list=[1,2,3,4,5]
number=4
result=custom_remove(user_list,number)
print(result)