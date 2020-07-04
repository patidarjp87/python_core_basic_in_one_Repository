print("program to count elements in a given set")
s1=set([eval(x) for x in input('enter elements for set 1 as it is as you want to see in your set with separator space\n').split()])
'''print(len(s1))'''
count=0
for x in s1:
    count+=1
print('no. of elements in given set is',count)
input()