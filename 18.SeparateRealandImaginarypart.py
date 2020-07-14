
c = input("enter a complex number")
i=0
while c[i]!='+':
   i=i+1
real=int(c[:i])
i=i+1
imag=c[i:]

j=0
while imag[j]!='j':
   j=j+1
imag=int(imag[:j])
print(real,type(real),imag ,type(imag))

if real>imag:
    print(real ,'is greater')
else:
    print(imag,'is greater')
  
input("press enter to exit")
