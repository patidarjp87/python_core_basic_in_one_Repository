
print('program to print all prime numbers between a and b')
a=int(input('enter a value of a'))
b=int(input('enter a value of b'))
if a==0:
 a+=1   
 for x in range(a+1,b):
     for y in range(2,x+1):
      if x%y==0:
          break
      else:
          continue
     if y==x:
       print(x,end=' ')
       if x!=b-1:
         continue
       else:
          break
     else :
      continue
else:
    for x in range(a+1,b):
     for y in range(2,x+1):
      if x%y==0:
          break
      else:
          continue
     if y==x:
       print(x,end=' ')
       if x!=b-1:
         continue
       else:
          break
     else :
      continue
input('press enter to exit')
