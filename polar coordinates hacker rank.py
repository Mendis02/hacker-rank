import cmath

#this doesn't work for negative values

s = input()
l = list(s)
if l[0] == "-":
  x=int(l[1])
  y = int(l[3])
else:
  
  x = int(l[0])
  y = int(l[2])


print(abs(complex(x, y)))
print(cmath.phase(complex(x, y)))
