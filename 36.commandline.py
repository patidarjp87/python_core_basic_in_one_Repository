from sys import argv
y=0
s=0
for x in argv:
    if y==0:
        y=1
    else:
        s=s+int(x)
print('sum is',s)
input()
