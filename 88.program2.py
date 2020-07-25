
print("script to write a function which takes a tuple of int values and returns a dict whose key are tuples value and values are frequency of ecah key in the tuple\n Takes tuple returns dict")
def fun(t):
    d={}
    fr=0
    l1=[]
    l2=[]
    i=0
    length=len(t)
    for x in t:
        count=0
        for y in t:
            if x==y:
                count+=1       
        else:
            if x not in l1:
                l1.append(x)
                fr=(count/length)*100
                l2.append(fr)
    while i!=len(l1):
           d[l1[i]]=l2[i]
           i+=1
    return d
t=eval(input('Enter a tuple of int values'))
d=fun(t)
print('dict of int values corresponding with their frequencies \n',d)
input()
