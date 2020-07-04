print('program to compare two tuples in any order\n Enter 1st tuple')
t1=eval(input())
t2=eval(input("Enter 2nd tuple\n"))
for x in t1:
    for y in t2:
        if x==y:
            break
    else:
        print('Tuples does not contain same element in any order')
        break
else:
    print('Tuples contain same element in any order')
input()

