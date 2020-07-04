print('program to print first N prime numbers')
N=int(input('enter a value of N'))
count=0
for x in range(2,10000):
    for y in range(2,x+1):
       if x%y==0:
           break 
       else:
            continue
    if y==x:
      print(x,end=' ')
      count+=1
      if count>=N:
          break
    else:
        continue
input('\npress enter to exit')

    
