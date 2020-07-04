print("script to find reverse binary representation of a given no\n takes something returns something\n Enter a no.")
n=int(input())
def binary(j):
  s=str()
  while j!=1:
    a=str(j%2)
    s=s+a
    j=int(j/2)
  s=s+str(j)
  return int(s)
print("Reverse of binary of",n,'is',binary(n))
input()
