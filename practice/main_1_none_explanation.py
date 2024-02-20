#Tip-1
#Append return NONE value
# a=[1,2,3,4,5]
# b=a.append(10)
# print(b)#output as NONE
#explanation
# None is a design choice made by the Python language developers
# . The rationale behind this design is to make it clear that the method is acting in-place
#  and directly modifying the object it is called on.

#Tip-2
#Memory
a=10
def fuc():
    global a
    a=[1,2,3,4,5]
    a.append(10)
    print(a)
fuc()
print(a)

# 'Above code a=10  ah next line la  print panna 10 varum
# adhae function kula  a va global variable mathuna ,function kulla ena value iruko
#  adhu dha All a ku varum or mari irukum after a va print panna'






