x = 2
x = 4
print(x)

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

cheeses = ['Cherr', 'adam', 'adil']
for cheese in cheeses:
    print(cheese)
numbers = [17,33,43,54]
empty = []
print(cheeses, numbers, empty)

print(cheeses[2])

numbers = [17,33,43]
numbers[2] = 5
print(numbers)

y=[0] * 4
print(y)

z= [1, 2, 3] * 3
print(z)

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])

d = ['p', 'r', 's', 'e', 'h', 'l']
d[1:3] = ['x', 'y']
print(d)

t = ['a', 'b', 'c']
t.append('d')
print(t)

s='spam'
t=list(s)
print(t)

a=[1,2,3]
b is a
print(b)

s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])

a = [1, 2, 3]
b = a
b is a
b[0] = 17
print(a)

def delete_head(t):
    del t[0]
letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)
t3 = t1 + [3]
print(t3)

def tail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)

my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()              
    for word in words:
        if word in my_list:
                continue                    
my_list.append(word)        
print(sorted(my_list))   

my_list = []                        
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))


   








