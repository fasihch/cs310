name = input("Write your name: ")
print("Hello", name, "!")

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
salary = hours * rate
print("Pay: {0:.2f}".format(salary))


width = 17
height = 12.0
print(width/2)
print(type(width/2))
print(width/2.0)
print(type(width/2.0))
print(height/3)
print(type(height/3))
print(1+2*5)
print(type(1+2*5))

from fractions import Fraction
celsius = float(input("Enter degrees in Celsius: "))
fahrenheit = celsius * Fraction(9, 5) + 32
print("{0:.2f} C⁰ is {1:.2f} F⁰".format(celsius, fahrenheit))

a = 35.0
b = 12.50
c =a*b
print(c)

hours =35.0
rate = 12.50
pay = hours * rate
print(pay)

name=input('What is your name?\n')
print(name)

first =10
second =15
print(first+second)

first='100'
second='110'
print(first+second)

first= 'fasih'
second= 'ahmed'
print(first+second)

first= 'test'
second= 3
print(first*second)

a=20+32-(40*5)*(15-7)
print(a)


