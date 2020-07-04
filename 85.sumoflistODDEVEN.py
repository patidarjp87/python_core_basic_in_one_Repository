print("script to sum of all even no. and sum of all odd no. from a given list\nTakes something returns something")
l=[eval(x) for x in input('Enter elements of list as it as you want to see in list by separator space').split()]
def sum(l):
    even=0
    odd=0
    for x in l:
        if x%2==0:
            even+=x
        else:
            odd+=x
    return even,odd
a,b=sum(l)
print('sum of even and odd numbers in a given list is respectively :: ',a,'and',b)
input()
