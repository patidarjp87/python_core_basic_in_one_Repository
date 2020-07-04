print("script to write a function which takes a list of strings as an arguments and returns a dict whose each key is a alphabet and list of strings begin with that alphabet")
l=eval(input('Enter a list'))
def fun(l):
    d={}
    s=str()
    for x in l:
        for y in x:
            s=y
            d.update({s:x})
            break
    else:
        return d
d=fun(l)
print('Returned required dict is',d)
input()