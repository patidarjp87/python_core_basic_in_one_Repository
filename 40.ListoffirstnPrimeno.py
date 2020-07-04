print('program to print list of first n prime no.\n enter a no n=')
n=int(input())
l=[]
count=0
for x in range(2,1000):
    for y in range(2,x):
        if x%y==0:
            break
        else:
            continue
    else:
        l.append(x)
        count+=1
    if count==n:
        break
print(l)
input()

