
print("program to create tuples with homogeneous elements from a tuple containing heterogeneous elements\n Enter a heterogeneous tuple")
p=eval(input())
t1=tuple()
t2=tuple()
t3=tuple()
t4=tuple()
t5=tuple()
t6=tuple()
t7=tuple()
t8=tuple()
t9=tuple()
for x in p:
    if type(x)==str:
        t1+=(x,)
    elif type(x)==int:
        t2+=(x,)
    elif type(x)==float:
        t3+=(x,)
    elif type(x)==complex:
        t4+=(x,)
    elif type(x)==list:
        t5+=(x,)
    elif type(x)==bool:
        t6+=(x,)
    elif type(x)==tuple:
        t7+=(x)
    elif type(x)==set:
        t8+=(x,)
    elif type(x)==dict:
        t9+=(x,)
print('tuples with homogeneous elements are :::')
print("tuple of string elements :-",t1)
print("tuple of integer elements :-",t2)
print("tuple of float elements :-",t3)
print("tuple of complex elements :-",t4)
print("tuple of list elements :-",t5)
print("tuple of boolean elements :-",t6)
print("tuple of tuple elements :-",t7)
print("tuple of set elements :-",t8)
print("tuple of dictionary elements :-",t9)
input()
