
l=eval(input('enter a list'))
round=1
length=len(l)
while round<length:
   i=0 
   while i<length-round: 
       if l[i]>l[i+1]:
        t=l[i]
        l[i]=l[i+1]
        l[i+1]=t
       i+=1
   round+=1
for x in l:
 print(x)
input()

