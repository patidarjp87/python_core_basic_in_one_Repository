print("program to print all possible subset of r elements from a given set of n elements ")
s1=set([eval(x) for x in input('enter elements for set 1 as it is as you want to see in your set with separator space\n').split()])
r=int(input('enter r =\n'))
n=len(s1)
s2=set()
c=0
while c>1:
 count=0
 for x in s1:
    if x not in s2:
     s2.add(x)
     count+=1
     if r==count:
        break
 print(s2)
 c+=1
input()
'''print("program to print all possible subset of r elements from a given set of n elements ")
s1=set([eval(x) for x in input('enter elements for set 1 as it is as you want to see in your set with separator space\n').split()])
j=int(input('enter r =\n'))
l=list(s1)
i=0
m=0
j=3
while j!=8:
 l1=[]
 for x in l:
     if i!=4:
      print(l[i:j:1],end=' ')
      i+=1
      j+=1
     else:
         m+=1
         break
 i=m
 j+=1
input()
 


     s2.add(x)
     count+=1
     if r==count:
        break
 t=t+(s2,)
 if c==0: 
   print(s2,end=' ')
   c+=1
 else:
    if s2 not in t:
        print(s2,end=' ')
        c+=1
    else:
        continue
input()
'''
