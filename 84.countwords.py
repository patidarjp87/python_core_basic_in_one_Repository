print("script to ciunt words in a given string \n Takes somthing returns something\n Enter a string")
s=input()
def count(s):
    l=s.split()
    return len(l)
print('no. of words in agiven string is ',count(s))
input()
