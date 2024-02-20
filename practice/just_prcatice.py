# find max number :
# input=[1,2,3,4,5,10]
# max_num=input[0]
# for x in input:
#     if x>max_num:
#         max_num=x
# print(max_num)

# ***************************************************************************


# sorting in ascending order:

# lenght=len(input)
# for x in range(lenght):
#     for y in range(x+1,lenght):
#         if input[x]>input[y]:
#             temp=input[x]
#             input[x]=input[y]
#             input[y]=temp
# print(input)
# ***************************************************************************
# sorting in decending order:
# a=[10,1000,100,1,2,3,4,5]
# len=len(a)
# for x in range(len):
#     for y in range(x+1,len):
#         if a[x]<a[y]:
#             temp=a[x]
#             a[x]=a[y]
#             a[y]=temp
            # alternate swap-1
            # a[x]=a[x]+a[y]
            # a[y]=a[x]-a[y]
            # a[x]=a[x]-a[y]
            # alternate swap-2
            # a[x]=a[x]^a[y]
            # a[y]=a[x]^a[y]
            # a[x]=a[x]^a[y]
# print(a)
# **************************************************************************** 
# largest number in three elements:
# a=10
# b=20
# c=39
# if a>b and a>c :
#     print("A is greater")
# elif b>a and b>c :
#     print("B is greater")
# elif c>a and c>b :
#     print("c is greater")
#  *********************************************************
# append user defined function:
# def custom_append(userlist,number):
#     newlist=userlist[:]
#     newlist[len(userlist):]=[number]
#     return newlist

# userlist=[1,2,3,4,5]
# number=10
# result=custom_append(userlist,number)
# print(result)
# ***************************************************************
# remove user defined function : 
# def custom_remove(userlist,num):
#     new_list=userlist[:]
#     access_indexes=userlist.index(num)
#     new_list=new_list[:access_indexes]+new_list[access_indexes+1:]
#     return new_list

# list=[1,2,3,4,5]
# n=2
# result=custom_remove(list,n)
# print(result)
# *********************************************************************
# print letters not a voeels and also print repeated letters 
# input='computered'
# vowels="aeiouAEIOU"
# result=""
# for x in input:
#     if x not in vowels or input.count(x)>2:
#         result+=x

# print(result)

