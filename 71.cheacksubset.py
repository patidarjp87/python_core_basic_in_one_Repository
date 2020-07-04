print("program to check whether a given set is a subset of another given set")
s1=set([eval(x) for x in input('enter elements in superset set 1 as it is as you want to see in your set with separator space\n').split()])
s2=set([eval(x) for x in input('enter elements subset set 2 as it is as you want to see in your set with separator space\n').split()])
if s2.issubset(s1):
    print('s2 is a subset of s1')
else:
    print("s2 is not a subset of s1")
input()