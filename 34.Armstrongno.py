print("program to print armstrong no. under 1000")
input('press enter to print')
for x in range(1,1000):
    a=x%10#5
    b=x//10#53
    c=b%10#3
    d=b//10#5
    y=(a**3)+(c**3)+(d**3)
    if x==y:
        print(x,end=' ')
    
input('\npress enter to exit')

