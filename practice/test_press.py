# # 1.Program to print the reverse of the given string 
user_input=input("Enter the word wants to reverse :")
Lowercase_user_input=user_input.lower()
reverse=""
for x in Lowercase_user_input:
    reverse=x+reverse
print(reverse)

# # 2.Program for given number is prime or not
user=int(input("Enter the number you want to check : ")) 
prime_numbers=[]
for x in range(user+1):
    if x>1:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            prime_numbers.append(x)
if user in prime_numbers:
    print("Given number is PRIME NUMBER")
else:print("Given number is NOT a prime number")

# # 3.Program to form largest value by arranging in given array
Input_array=[100,10, 52, 66, 99]
Input_array.sort(reverse=True)
for x in Input_array:
    print(x,end="")

# # 4. Program to find reverse of number 
user_input=100
String_converson=str(user_input)
result=String_converson[::-1]
print(int(result))

#  note answer-when converting string to integer in python,the leading zeros are ignored in numerical values

 # 5. program to find maxi and mini element in given array 
def min(user_input):
    min_value=user_input[0]
    for x in user_input:
        if x<min_value:
            min_value=x
    return min_value
def max(user_input):
    max_value=user_input[0]
    for x in user_input:
        if x>max_value:
            max_value=x
    return max_value
user_input=[54,546,548,60]
minimum_value=min(user_input)
maximum_value=max(user_input)
print(maximum_value,minimum_value)
 