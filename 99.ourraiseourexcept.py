print('script of Exception handling our raise default except but our message')
x=int(input('enter first no'))
y=int(input('enter second no'))
try:
    if y==0:
        raise ZeroDivisionError('Denominator can not be zero')
    z=x/y
except ZeroDivisionError:
    print("Exception :Denominator can not be zero")
else:
    print('division is',z)
finally:
    print("press enter to exit")
input()
