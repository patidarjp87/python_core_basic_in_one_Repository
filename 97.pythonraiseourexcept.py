
print('script of Exception handling default raise our except')
x=int(input('enter first no'))
y=int(input('enter first no'))
try:
    z=x/y
except ZeroDivisionError:
    print('Exception:Denominator can not be zero')
else:
    print('division is',z)
finally:
    print('press enter to exit')
input()
