n=int(input('enter a no to cheak prime'))
i=0
if n==1:
    print(n,'is not a prime no.')
if n>1:
 while i!=1:
  for x in range(2,n):
    if n%x==0:
        break
    else:
        continue
  if x==n-1:
    print(n,'is a prime no.')
  else:
    print(n,'is not a prime no.')
  i+=1
input("prees enter to exit")


