'''FIRST'''
print('program to reverse a given tuple\n Enter  a tuple')
p=eval(input())
print('reversed tuple is',p[::-1])
input('press enter to exit')
'''
SECOND
t=tuple(input('press enter to see reversed tuple'))
for x in p:
    t=(x,)+ t
print('reversed tuple is ::',t)
input()

THIRD
l=list(p)
l1=[]
for x in l:
    l1=[x]+l1
print('reversed tuple is ::',tuple(l1))
input()

FOURTH
l=list(p)
l.reverse()
print('reversed tuple is ::',tuple(l))
input()

FIFTH
l=list(p)
length=len(l)
i=0
while i<length//2:
     t=l[i]
     l[i]=l[length-1-i]
     l[length-1-i]=t
     i+=1
print('reversed tuple is ::',tuple(l))
input()'''


