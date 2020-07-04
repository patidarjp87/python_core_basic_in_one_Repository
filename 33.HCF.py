print('HCF of two no. is the largest number that divides both of them')
print('LCM of two numbers a and b \n enter a numbers')
a=int(input())
b=int(input())
if a>b:
   for x in range(a,1,-1):
     if a%x==0 and b%x==0:
       print(x,'is the HCF of',a,'and',b)
       break
     else:
       continue
   if x==2:
       print('there is no HCF of',a,'and',b)
else:
    for x in range(b,1,-1):
     if a%x==0 and b%x==0:
       print(x,'is the HCF of',a,'and',b)
       break
     else:
       continue
    if x==2:
       print('there is no HCF of',a,'and',b)
input('press enter to exit')

