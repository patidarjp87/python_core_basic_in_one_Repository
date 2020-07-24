
print("script to calculate LCM of two no. using takes something returns somthing function")
l=[int(x) for x in input("enter two numbers by separator space").split()]
def LCM(a,b):
 for p in range(max(l),a*b+1):
    if p%a==0 and p%b==0:
        return p
 else:
     return 0
x,y=l
s=LCM(x,y)
if s!=0:
    print("LCM of",x,"and",y,"is ",s)
else:
    print("there is no LCM bw",x,"and",y)

input()
