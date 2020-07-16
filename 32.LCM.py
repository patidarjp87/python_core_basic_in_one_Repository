
print('LCM of two numbers a and b \n enter a numbers')
a=int(input())
b=int(input())
if a>b:
    for x in range(a,a*b+1):
        if x%a==0 and x%b==0:
            print(x,'is the LCM of ',a,'and',b)
            break
        else:
            continue
else:
    for x in range(b,a*b+1):
        if x%a==0 and x%b==0:
            print(x,'is the LCM of ',a,'and',b)
            break
        else:
            continue
input("press enter to exit")

