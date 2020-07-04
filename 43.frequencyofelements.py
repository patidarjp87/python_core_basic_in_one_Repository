print('print distinct list of elements along with their frequency of occurence\n Enter a list')
l=eval(input())
length=len(l)
p=[]
fr=0
for x in l:
    count=0
    for y in l:
        if y==x:
            count+=1
    else:
       if x not in p:
         p.append(x)
         fr=(count/length)*100
         print('frequncy of element',x,'is',fr,'%')
input('enter press to exit')

