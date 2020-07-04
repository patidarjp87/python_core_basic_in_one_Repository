s1=input("enter a string")
s2=input("enter a string")
s3=input("enter a string")
i=1
while i<=1:
 if s1<s2:
    i=i+1
    pass
 else :
  t=s1
  s1=s2
  s2=t
  i=i+1
  if s2<s3:
    i=i+1
    pass
  else:
    i=i+1
    t=s2
    s2=s3
    s3=t
print(s1,s2,s3)
input("press enter to exit")

