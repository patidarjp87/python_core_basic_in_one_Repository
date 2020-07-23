
print("program to find common elements bw two sets ")
s1=set([eval(x) for x in input('enter elements for set 1 as it is as you want to see in your set with separator space\n').split()])
s2=set([eval(x) for x in input('enter elements for set 2 as it is as you want to see in your set with separator space\n').split()])
s=s1.intersection(s2)
print('common elements between s1 and s2 are :-')
for x in s:
   print(x,end=',')
input()
