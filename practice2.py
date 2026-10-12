name=input("Enter your name:")
age = int(input("enter your age:"))
height=float(input("enter your height:"))
_adult=age>=18
favorite_number=int(input("enter your favourite number:"))
print("next year you will be"+str(age+1))
print(_adult)
if favorite_number==10:
    print("your number is exactly 10")
elif favorite_number<10:
    print("your number is small")
else:
    print("your number is big")
print(age*2)
print(favorite_number**2)
print(favorite_number/2)
print(favorite_number//2)
print(favorite_number%2)
