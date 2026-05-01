hello = "hello world"
print(hello)

n1=7
print(n1)
n2=3
print(n2)
c = n1 + n2
print(c)

n1 = 99
print(n1)

myname = "gio"
print("my name is " + myname)


##########

myname= "gio"
print("welcome to " + myname)

my_name = "ren"
print("welcome to",  myname + " "  + my_name + " age of", 26)

age = 1

for x in range(10):
     print("my_name")

for y in range(20):
    print(age)
    age = age + 1


for x in range(10):
    print(x, "welcome home")
    x = x + 1

for b in range(5):
    print('hello b',)
    for b in range(5):
        print(b, "hello bb")


n1=10
n2=20
total= n1 + n2
print("total", total)


n1=10
n2=20
total= n1 + n2
print("total", total)

n1=int(input("enter first number"))
n2=int(input("enter second number"))
total= n1 + n2
print("total", total)




n1=10
n2=20
total= n1 + n2
print("total", total)

n1=int(input("enter first number"))
n2=int(input("enter second number"))
total= n1 + n2
print("total", total)



# importing calendar module

import  datetime
import calendar



# To take month and year input from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day:"))

# display the calendar
print(calendar.month(year, month))
print(datetime.date(year, month, day))



from datetime import date


# To take month and year input from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day:"))

# display the calendar
print(date(year, month, day))


n1=float(input('enter first number:'))
n2=float(input('enter second number:'))

print("total:", n1+n2)

print('total', n1-n2)

print('total', n1*n2)

print('left over', n1 % n2)

print('left over', n1 // n2)


number1= float(input("enter first number"))
number2= float(input("enter second number"))

operator= input('enter operator (+,-,*)')
if operator=='+':
    print(number1+number2)
elif operator=='-':
    print(number1-number2)
elif operator=='*':
    print(number1*number2)
elif operator=='/':
    print(number1/number2)
else:
    print('invalid operator')

name = input("enter your name:")
age = int(input("enter your age:"))

print("Welcome " + name)
print("you will be " + str(age + 1) + " next year")







