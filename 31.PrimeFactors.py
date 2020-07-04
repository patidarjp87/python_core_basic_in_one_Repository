print('program to print all prime factors of a no. n \n enter a value of n')
n=int(input())
print(1,end=' ')
if n>1:
   for x in range(2,n+1):
    if n%x==0:
        for y in range(2,x+1):
           if x%y==0:
               break
           else :
                continue
        if y==x:
          print(x,end=' ')
          continue
        else :
            continue
input("press enter to exit")

