
print('script of Exception handling user defined Exception our raise default except our message')
class InsufficientBalance(ZeroDivisionError):
    def __init__(self,m):
        self.msg=m
class InvalidWithdrawAmount(InsufficientBalance):
    def __init__(self,m):
        self.msg=m        
balance=5000
print('Your accout balance is',balance)
w=eval(input('Enter amount to withdraw in multiple of 100\n'))
try:
    if w>balance:
        raise InsufficientBalance('Insufficient balance in the accout')
    elif w%100!=0:
        raise InvalidWithdrawAmount('Entered amount may not be multiple of 100')
    else:
        print('Withdraw successful...!!!')
except InsufficientBalance as i:
    print('Exception raised:',i.msg)
except:
    print('Default Error')
else:
    balance-=w
finally:
    print('Updated balance is',balance)
input()
