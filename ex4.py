import random

for i in range(10):
    x = random.random()
    print(x)

def print_lyrics():
    print("I'm a fasih I'm okay.")
    print('I sleep all night and I work all day.')

print_lyrics()


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('Spam')
print_twice(17)
print_twice('Spam '*4)

michael = 'Eric, the half a bee.'
print_twice(michael)

result = print_twice('Bing')

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)


def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()


def computepay(tmp_hours, tmp_rate):
    
    if tmp_hours <= 40.0:
        return tmp_rate * tmp_hours                

    overtime = tmp_hours - 40.0              
    return (tmp_rate * 40.0) + (1.5 * tmp_rate * overtime)


def check_for_float(input1):
   
    try:
        val = float(input1)                
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()


input_hours = input('Enter Hours: ')
hours = check_for_float(input_hours)

input_rate = input('Enter Rate: ')
rate = check_for_float(input_rate)

pay = computepay(hours, rate)
print('Pay: ', pay)




