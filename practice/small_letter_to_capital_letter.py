a="manojKUMAR"
ans=""
for x in a:
    if x==x.upper():
        ans+=x.lower()
    else:
        if x==x.lower():
            ans+=x.upper()
print(ans)