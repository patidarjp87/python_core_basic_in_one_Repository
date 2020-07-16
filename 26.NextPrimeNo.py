
n=int(input('enter a no.'))
if n==0:
 n=n+1   
 for x in range(n+1,n+101):
  for y in range(2,x+1):
     if x%y==0:
         break
     else:
         continue
  if y==x:
     print(x,'is the next prime no. after ',n)
     break
  else:
     continue
else:
    for x in range(n+1,n+101):
      for y in range(2,x+1):
       if x%y==0:
         break
       else:
          continue
      if y==x:
        print(x,'is the next prime no. after ',n)
        break
      else:
        continue
input()
  
