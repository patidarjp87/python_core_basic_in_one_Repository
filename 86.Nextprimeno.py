
print("program to print next prime no. of a given no. \n Takes something returns something\n Enter a no.")
n=int(input())
def nextprime(n):
    for x in range(n+1,n+100):
        for y in range(2,x):
            if x%y==0:
                break
        else :
            return x
            break
r=nextprime(n)
print("prime no. after",n,"is",r)
input()
