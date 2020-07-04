print("sun of all even no. and sum of all odd no\n Enter a list")
l=eval(input())
even=0
odd=0
for x in l:
    if x%2==0:
        even+=x
    else:
        odd+=x
print('sum of even no. is',even,'sum of odd no. is',odd)
input()
