
#f = open('demofile.txt','xt')
#ff = open('test.txt','x')
f1 = open('demofile.txt','rt')
print(f1.read())


print()

f2 = open('demofile.txt','rt')
print(f2.read(5))

print()

f3 = open('demofile.txt','rt')
print(f3.readline())
print(f3.readline())

f4 = open('demofile.txt','rt')
for lines in f4:
    print(lines)

f5 = open('demofile.txt','a')
f5.write('\nappend practising')
f5.close()
f5 = open('demofile.txt','r')
print(f5.read())

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()


# for deleting a file

import os

if os.path.exists('test.txt'):
    os.remove('test.txt')
    print('test.txt remove successfully')
else:
    print('file does not exists')