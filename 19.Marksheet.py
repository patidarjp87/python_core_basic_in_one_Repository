s1=float(input('enter marks of 1st subject'))
s2=float(input('enter marks of 2nd subject'))
s3=float(input('enter marks of 3rd subject'))
s4=float(input('enter marks of 4th subject'))
s5=float(input('enter marks of 5th subject'))
if s1<=100 and s2<=100 and s3<=100 and s4<=100 and s5<=100:
 if s1>35 and s2>35 and s3>35 and s4>35 and s5>35:
  print("The student whose marks mentioned above is pass")
 else:
  print("The student whose marks mentioned above is fail")
 avg=(s1+s2+s3+s4+s5)/5
 if avg<=100:
  print("percentage is",avg,"% with grade" ,end=' ')
 if avg<35:
  print("F")
 elif avg<40:
  print('P')
 elif avg<50:
  print('C')
 elif avg<60:
  print('B')
 elif avg<70:
  print('B+')
 elif avg<80:
  print('A')
 elif avg<90:
  print('A+')
 elif avg<100:
  print('O')
 else:
  print("invalid marks or entered marks are out of 100")
else:
  print("invalid marks or entered marks are out of 100")
input()
