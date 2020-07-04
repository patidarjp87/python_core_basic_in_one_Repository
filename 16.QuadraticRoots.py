a=float(input('enter a coficient of x^2'))
b=float(input('enter a coficient of x'))
c=float(input('enter a constant'))
D=(b**2)-4*a*c
if D==0:
    print("equal roots are")
    roots = -b/(2*a)
    print("Roots = ",roots)
elif D<0:
    print("imaginary roots")
    root1 = (-b+(D**0.5))/(2*a)
    root2 = (-b-(D**0.5))/(2*a)
    print("root1 = ",root1,"root2 =",root2)
elif D>0:
    print("real roots")
    root1 = (-b+(D**0.5))/(2*a)
    root2 = (-b-(D**0.5))/(2*a)
    print("root1 = ",root1,"root2 =",root2)
    
input("press enter to exit")

