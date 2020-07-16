
print('numbers which do not have any common factor between them,are called co-prime factors')
print('enter a value of a and b')
a=int(input())
b=int(input())
if a>b:
 for x in range(2,b+1):
  if a%x==0 and b%x==0:
      print(a,'&',b,'are not co-prime numbers')
      break
  else:
      continue
 if x==b:
     print(a,'&',b,'are co-prime numbers')
else:
 for x in range(2,a+1):
  if a%x==0 and b%x==0:
      print(a,'&',b,'are not co-prime numbers')
      break
  else:
      continue
 if x==a:
     print(a,'&',b,'are co-prime numbers')   
input('press enter to exit')
