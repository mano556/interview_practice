# max num 
# a=[100,10,52,66,99,1000]
# max_num=a[0]
# for x in a:
#     if x>max_num:
#         max_num=x
# print(max_num)
# *********************************************
# a=[100,10,52,66,99,1000]
# b=len(a)
# for x in range(b) :
#     for y in range(x+1,b):
#         if a[x]<a[y]:
#             temp=a[x]
#             a[x]=a[y]
#             a[y]=temp
# print(a)
# **************************************************
 # 3.Program to form largest value by arranging in given array
# Input_array=[100,10, 52, 66, 99]
# lenght_of_input=len(Input_array)
# # indexes looping
# for x in range(lenght_of_input):
#     for y in range(x+1,lenght_of_input):
#         # comparing
#         if Input_array[x]<Input_array[y]:
#         #    swapping
#             Input_array[x]=Input_array[x]+Input_array[y]
#             Input_array[y]=Input_array[x]-Input_array[y]
#             Input_array[x]=Input_array[x]-Input_array[y]
            
# for x in Input_array:
#     print(x,end="")
# *******************************
# 4. Program to find reverse of number 
a=int(input('Enter the number you want to reverse :'))
temp=a
reverse=0
while temp>0:
    last_digit= temp%10
    reverse=reverse*10+last_digit
    temp=temp//10
print(reverse)
     
   
 
