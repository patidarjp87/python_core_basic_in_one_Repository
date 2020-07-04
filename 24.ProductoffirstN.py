n=int(input('enter a no. for products'))
sum=1
i=1
while i<=n:
  sum = sum * i
  i=i+1
print("product of first",n,"natural no. is",sum)
sum=1
i=1
while i<=n:
  sum = sum*(2*i-1)
  i=i+1
print("product of first",n,"odd natural no is",sum)
sum=1
i=1
while i<=n:
  sum = sum*(2*i)
  i=i+1
print("product is",n,"even natural no. is",sum)
input("pree enter to exit")

