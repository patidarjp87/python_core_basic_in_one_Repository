print("print Square of numbers from a to b\n enter values of a and b")
a=int(input())
b=int(input())
for x in range(a,b+1):
  print(x**2,end=' ')
print('use of range \nenter step size s and boundary values a and b')
s=int(input())
a=int(input())
b=int(input())
for x in range(a,b+1,s):
 print(x,end=' ')
input("\npress enter to exit")

