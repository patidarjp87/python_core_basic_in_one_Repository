print("program to create set of first n prime no\n Enter n=")
n=int(input())
count=0
for x in range(2,1000):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=' ')
        count+=1
        if count==n:
            break
input()
