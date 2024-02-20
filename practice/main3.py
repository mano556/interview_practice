
# class Dog:
#     def __init__(self,name,age,breed):
#         self.name=name
#         self.age=age
#         self.breed=breed
#     def __str__(self):
#         return f"{self.name}{self.age}{self.breed}"
# Dog_1=Dog("benny",5,"pug")
# Dog_2=Dog("steffy",4,"pug")
# Dog_3=Dog("Candy",7,"Labrador")

# print(Dog_1)
# print(Dog_2)
# print(Dog_3)

# print(f"{Dog_1.name} as a age of {Dog_1.age} with breed name {Dog_1.breed}")


# class int:
#     def __init__(self,number):
#         self.number=number
#     def __str__(self):
#         return f"{self.number}"
     
# x=int(5)
# print(x)



class IntClass:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Input must be an integer.")
        self.value = value

    def __str__(self):
        return f"{self.value}"

class FloatClass:
    def __init__(self, value):
        if not isinstance(value, float):
            raise ValueError("Input must be a float.")
        self.value = value

    def __str__(self):
        return f"{self.value}"

a=FloatClass(5.8)
print(a)


