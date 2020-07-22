
print('program to merge sorted tuple')
turn=1
while turn<3:
 print('Enter tuple',turn,':::')
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
     if turn==1:
        first=tuple(l)
        turn+=1
     else:
        second=tuple(l)
        turn+=1
print('combination of both sorted tuple is:::',first+second)  
input()

