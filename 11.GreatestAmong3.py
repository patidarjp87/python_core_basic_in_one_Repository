
'''a=float(input('enter first no.'))
b=float(input('enter Second no.'))
c=float(input('enter Third no.'))
if (a>b and a>c):
    print("%f is greater" %a)
elif (b>c and b>a):
    print("%f is greater" %b)
else:
    print("%F is greater" %c) '''

a=float(input('enter first no.'))
b=float(input('enter Second no.'))
c=float(input('enter Third no.'))
if a>b:
    if a>c:
        print("%f is greater"%a)
    else:
        print("%f is greater"%c)
elif b>c:
        print("%f is greater"%b)
else:
        print("%f is greater"%c)
input()
