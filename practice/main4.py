# remove duplicates
a=[1,1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,4]
b=[]
c=[]
for x in a:
    if x not in b:
        b.append(x)
    else:
        c.append(x)
print(b)
# print(c)