print("program to cheak whether a tuple is a subset of another tuple or not \n Enter super tuple")
t1=eval(input())
t2=eval(input("Enter child tuple\n"))
for x in t2:
    for y in t1:
        if x==y:
            break
    else:
        print(t2,"is not a subset of",t1)
        break
else:
    print(t2,"is a subset of ",t1)
input()
