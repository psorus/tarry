from genmaze import *
from collatz import *

from tarry import *

# x=arrmaze()
x=collatz()


print(timestat(x,simplesolve))
print(timestat(x,tarry_))
print(timestat(x,tarry))

exit()

print(x)


# x,steps=simplesolve(x)
x,steps=tarry(x)

print("needed steps",steps)

print(x)
