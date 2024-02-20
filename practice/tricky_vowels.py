user='coaeioumpuuterrrrr'
vowels="aeiou"
ans=""
# for x in user:
#     if x not in vowels or user.count(x) >=2:
#         ans+=x
# print(ans)
        
for x in user:
    if x not in vowels or user.count(x)>2:
        ans+=x
print(ans)