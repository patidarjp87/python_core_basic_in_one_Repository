
print("program to find union bw two sets")
s1=set([eval(x) for x in input('enter elements for set 1 as it is as you want to see in your set with separator space\n').split()])
s2=set([eval(x) for x in input('enter elements for set 2 as it is as you want to see in your set with separator space\n').split()])
print('union is :::',s1.union(s2))
input()
