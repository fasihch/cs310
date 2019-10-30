#Examples chapter 3
a= 12
print(type(a))
b=7.0
print(type(b))
fasih= "this is python"
print(type(fasih))

if 5 < 10 :
    print("5 is less than 10")
else:
    print("5 is bigger than 10")
if 10==10 :
    print("they are equal")
else :
    print("they are not equal")

inp= input("temp in fahrenheit:")
fahr=float(inp)
celsius=(fahr-32.0)* 5.0/9.0
print(celsius)

inp= input("temp in fahrenheit:")
try:
    fahr=float(inp)
    celsius=(fahr-32.0)* 5.0/9.0
    print(celsius)
except:
    print('please enter a number')
    
#ex3.1

def pay(hours,rate):
inp = int(input('enter number')
rate= int (10)

hours=input('enter number:')
try:
    w_hours=int(hours)
except:
    w_hours=-1
if(w_hours<=40):
    pay=(w_hours*10)
    print(pay)
else :
    pay=40*10+(w_hours-40)*15
    print(pay)
    
#ex3.2

hours = input('Enter Hours: ')
try:
    float(hours)>=0
except:
    print('error_msg_numeric')
    hours =input('Enter Hours: ')

rate =input('Enter rate: ')
try:
    float(rate) >=0
except:
    print("error_msg_numeric")
    rate = input('Enter Rate: ')
hours = float(hours)
rate = float(rate)

if hours > 40:
    extra_pay=hours-40
else:
    extra_time = 0

extra_pay = 0.5 * rate * extra_pay
pay = hours * rate + extra_pay
print (pay)

#ex3.3

def computegrade(score):
    if score > 1 or score < 0: return "Bad score"

    if score >= 0.9:
        return"A"
    elif score >= 0.8:
        return"B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"

try:
    score = float(input("Enter score: "))
    print(computegrade(score))
except :
    print("Bad score")
    exit()
    
#Finish

