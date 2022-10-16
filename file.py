
# reading from a file

exmpl = open('example.txt','r')
print('name of file : ', exmpl.name)
print('mode of file : ', exmpl.mode)
print('type : ', type(exmpl))
content = exmpl.read()
print('Contents : ')
print(content)
print()
exmpl.close()


# another way of opening a file
# this way is better because you don't need to close the file

with open('example.txt','r') as file1:
    content = file1.read()
    print('Contents inside from with : ')
    print(content)
    print()

with open('example.txt','r') as file1:
    # reading first 10 characters
    print('first 10 characters : ')
    print(file1.read(10))
    print()

with open('example.txt','r') as file1:
    # read one line
    print(file1.readline(), end='')
    print(file1.readline(), end='')
    print(file1.readline(), end='')
    print()
print()
with open('example.txt','r') as file1:
    i = 1
    for line in file1:
        print('line {} : '.format(i), line, end='')
        i = i+1
    print()
print()

with open('example.txt','r') as file1:
    # read all lines together
    # it will return a List

    contentList = file1.readlines()
    print('Line 1 : ', contentList[0])

# writing in a file

with open('example2.txt','w') as file1:
    file1.write('line 1\n')
    file1.write('line 2\n')

#nested file using

with open('example.txt','r') as readFile:
    with open('example3.txt','a') as writeFile:
        for line in readFile:
            writeFile.write(line)