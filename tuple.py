'''
def oddTuple(tup):
  new_tup = ()
  for i in range(0,len(tup),2):
    new_tup += tup[i:i+1]

  return new_tup


a = [0, 1, 3, 4,7]
b = [8,9,11]
a.insert(0, 100)
a.remove(3)
print(b.remove(1))
'''

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print(aList is bList)
