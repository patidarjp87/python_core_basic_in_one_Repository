
print("script to print first n prime no. \n Takes something returns nothing\n Enter n")
n=int(input())
def prime(n):
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
print('first',n,'prime numbers are :-')
prime(n)
input()



