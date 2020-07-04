common functions of list ,tuple and string :-

l.index(object,start],stop[) # works in forward way  #value error
l.count(object)
len(l)
l[big]:end[:step]      # works in both way if step>0 work forward   #value error
                                            # else work backward

common functions of list and tuple :-
max(l)
min(l)

functions of list :-
          
l.sort()
l.reverse()
l.clear()

l.pop(index)       #value error
l.remove(object)   #value error
l.append(object)
l.insert(index,object)

functions of string :-

l=s.split(sep=NOne,maxsplit=-1) # return list of strings
s=s.upper()
s=s.lower()
s=s.capitalize()

s.isupper()
s.islower()
s.isnumeric()
s.startswith(sub)
s.endswith(sub)

functions of set :-

s.add(object)
s.update(iterable sequence)
s.clear()

s.discard(object)
s.remove(object)       # may gives error if object not in set
s.pop()          # due to no concept of indexing pop function remove and return Random value from set ,may gives error if object not in set

s=s1.intersection(s2)
s=s1.union(s2)

s2.issubset(s1)
s1.issuperset(s2)

s=s1.copy()

functions of dict:-
d.update({key:value})
d[new key]= value

d[key]   # returns value  may gives error
d.get(key)      # returns value   does not gives error

del(d[key])         # delete pair or item
d.pop(key)   #remove item and returns value error if key not in dict
d.popitem()         # return and remove item 
d1=d.copy()
d.clear()

d1=d.items()
d1=d.keys()
d1=d.values()

d.setdefault()

d1=d.fromkeys(iterable sequence , value)
