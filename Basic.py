
#printing

print('hello world')


#assigning multiple values
x,y,z = 2,3,4
print(x,y,z)

#unpack values of list or tuple

fruits = ['apple','banana','guava']
x,y,z = fruits
print(x,y,z)

#string

s = 'python is fun'
print(s)
for i in s:
    print(i, end='')
print()
print()

# cheacking a string is present in another string or not

s1 = 'python is fun'
s2 = 'python'
s3 = 'py'
s4 = 'pyo'

print(s2 in s1)
print(s3 in s1)
print(s4 in s1)

#cheacking not present

print(s4 not in s1)
print()

#slicing

s = 'asdfghjkl'

print(s[2:5])   #2 to <5
print(s[:5])    # from start
print(s[6:])    # upto end
print(s[0:7:2]) # gap will be 2-1
print(s[-5:-2])
print()

#string methods

s = 'asdfGhjkl'

print(s.upper())
print(s.lower())
t = '    were, kke, oerr    '
print(t)
print(t.strip())  #remove whitespace
print(t.replace('e','b'))   # replace all occurence of 'e' with 'b'
print(t.replace('e','b',2)) # replace first two occurence of 'e' with 'b'
print(t.split(','))
print()

#format method

age = 22
cls = 10
txt = 'My name is Redowan and I am {} years old and I am now at class {}'
print(txt.format(age,cls))
print()

x = 2
y = 3
print(x**y)  # exponentiation
print(y//x)  # floor divition
print()

# logical operators (and,or,not)

x = 5
y = 0

if x and y:
    print('x and y both are non zero')
else:
    print('not non zero')
print()

# comparison operator (is , is  not)

if x is y:
    print('same object')
else:
    print('not same object')
print()

# membership operator (in, not in)

# list (ordered,changeable,allow duplicates)

myList = ['apple','banana','cherry','guava',]
print(myList)
print(myList[0])
print(myList[-1])  # last item

if 'apple' in myList:
    print('exist')
else:
    print('not exist')

myList[0] = 'strawberry'
myList[1:3] = ["blackcurrant", "watermelon"]
print(myList)
myList.insert(2,'banana')
myList.append('orange')
print(myList)

myList.remove('watermelon')
myList.pop(1)
# del myList ---> remove whole list
print(myList)

#looping through list

for item in myList:
    print(item,end=' ')
print()

for i in range(len(myList)):
    print(myList[i], end=' ')
print()

#list comprehension (later)

#sorting list

myList.sort()
print(myList)
numbers = [10,4,100,1,1000,234]
numbers.sort()
print(numbers)

# reversing list

myList.sort(reverse = True)
numbers.sort(reverse = True)
print(myList)
print(numbers)

# another way of sorting : numbers.sort(key = funcName)
# myList.sort(key = str.lower)
# myList.reverse()

# copying a list
'''
myList2 = myList will only create a reference
change in myList2 will also take place in myList
'''

myList2 = myList.copy()
print(myList2)

# list3 = list1 + list2
# list1.extend(list2)

print()

# tuple

myTpl = ("apple", "banana", "cherry")
print(myTpl)
# tuple's are immutable
# we cannot change, add or remove items
# allows duplicates values
# if we want to change a tuple, we can convert it to list, then change the list and convert it to tuple
x,y,z = myTpl
print(x,y,z)
print(myTpl.count('apple'))
print(myTpl.index('cherry'))
print()

# set

mySet = {'apple',1,True,34.55,'banana',1,'1'}
print(mySet)
# we can add items to set
mySet.add('cow')
print(mySet)
# we can use update method to add a iterable object into another set
mySet.discard('1')     # removing item (remove method will rise error if item not found)
print(mySet)
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
print(set1.union(set2))
print(set1.intersection(set2))
print()

# dictionary

myDict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

print(myDict)
print(myDict['brand'])
print(myDict.keys())
myDict['colors'] = ['red','white','grey']
print(myDict)
print(myDict.values())
print(myDict.values())
print(myDict.items())
myDict.pop('year')
print(myDict)

# looping

for key in myDict:
    print(key,' : ',myDict[key])

for key,value in myDict.items():
    print(key, ' : ', value)

dict2 = myDict.copy()
print(dict2)

print()

# if else

a = 8

if a==0:
    print('zero')
elif a%2==0:
    print('even')
else:
    print('odd')
# if in one line

if(a%2==0) : print('a is even')

#if else in one line

print('even') if a%2==0 else print('odd')

# we can use pass statement if our if body has no content

print()

# while loop

i = 1

while i<=5:
    print(i)
    i+=1
else:
    print('i is now greater than 5')
print()

# for loop

numbers = [1,3,5,7,2]

for i in numbers:
    print(i)
else:
    print('loop finish')

for i in range(6):  #  (0-5)
    print(i)
else:
    print('loop finish')

for i in range (1,10,2):
    print(i)
print()

x = ['red','blue','green']
y = ['apple','banana','cherry']

for i in x:
    for j in y:
        print(i,j)
print()

# function

def call(name):
    print('hello ',name)

def add(a,b):
    return a+b

call('red')
call('python')
print(add(2,3))
print(add('red','1'))
# print(add('red',1))

def func(*name):
    for x in name:
        print(x,end=' ')
    print()

func('joe','alan','piky')

def key_value(c1,c3,c2):   # order doesn't matter
    print(c1,' ',c2,' ',c3)

key_value(c1='1',c2='2',c3=3)

#recursion

def fact(n):
    if(n<=1):
        return n
    else:
        return n*fact(n-1)

print('factorial of 5 : ', fact(5))
print()