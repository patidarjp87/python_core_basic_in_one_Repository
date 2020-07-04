print("function to find nth term of fibonacci series \n Takes something returns something")
n=int(input('Enter n =  '))
def fibonacci(n):
    l=[0,1]
    count=1
    i=0
    while count!=n:
      sum=l[i+1]+l[i]
      l.append(sum)
      count+=1
      i+=1
    return sum
term=fibonacci(n)
print(n,"th term of fibomacci series is ",term)
input()