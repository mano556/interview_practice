# Find average of numbers
# Ask how many numbers and get those number from users and  find 
user=int(input("How many numbers : "))
total=0
for x in range (user):
    numbers =int(input("Enter the numbers : "))
    total+=numbers
ans=total/user
print(ans)