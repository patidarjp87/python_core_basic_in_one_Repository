
print('program to sort list and find greatest no.in the list')
'''l=eval(input('enter a list'))
length=len(l)
i=0
j=0
while j!=length-1:
      if l[i]<l[j+1]:
       t=l[j+1]
       l[j+1]=l[i]
       l[i]=t
      j+=1
print('greatest no.is',l[0])
input()'''
       
l=eval(input('enter a list'))
l.sort()
print('sorted list is',l)
print('greatest no. is',l[len(l)-1])
input()

