
print("program to print greatest int in a given heterogeneos tuple \n Enter a tuple")
t=eval(input())
t1=tuple()
for x in t:
    if type(x)==int:
        t1+=(x,)
print ("Tuple of integers in Tuple  ",t,"is    :-",t1)
r=1
l=list(t1)
length=len(l)
while r<length:
    i=0
    while i<length-r:
        if l[i]<l[i+1]:
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
        i+=1
    r+=1
else:
    print("greatest no. in tuple is ",l[0])
input()
