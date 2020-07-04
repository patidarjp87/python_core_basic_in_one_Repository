print("program to calculate frequency of elements of tuple \n Enter a tuple")
t=eval(input())
fr=0
l=[]
length=len(t)
for x in t:
    count=0
    for y in t:
        if x==y:
            count+=1
    else:
       if x not in l: 
        fr = count/length
        print('frequency of',x,'is ',fr*100)
        l.append(x)
t=tuple(l)
print('tuple without duplication of elements is',t)
input()
