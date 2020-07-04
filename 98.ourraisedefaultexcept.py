print('script of Exception handling our raise default except but our message')
x=int(input('enter first no'))
y=int(input('enter first no'))
if y==0:
    raise ZeroDivisionError('Denominator can not be zero')
z=x/y
print('division is',z)
input()
