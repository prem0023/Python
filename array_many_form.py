from array import *

vals = array('i',[5,6,8,9,7])
print(vals)

vals = array('i',[5,6,8,9,7])
print(vals.buffer_info())

vals = array('i',[5,6,8,9,7])
vals.reverse()
print(vals)

print()

vals = array('i',[5,6,8,9,7])
for i in range(len(vals)):
    print(vals[i])

print()

vals = array('i',[5,6,8,9,7])
for a in vals:
    print(a)

print()

vals = array('i',[5,6,8,9,7])
newarr = array(vals.typecode, (a for a in vals))
for e in vals:
    print(e)
