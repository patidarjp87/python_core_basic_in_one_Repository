print('program to sort tuple elements \n Enter a tuple')
p=eval(input())
l=list(p)
length=len(l)
r=1
while r<length:
    i=0
    while i<length-r:
        if l[i]>l[i+1]:
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
        i+=1
    r+=1
else:
    p=tuple(l)
    print('sorted tuple is',p)
input()

