x = open("03.dat","rt").read()

t = ['.'+r+'.' for r in x.strip().splitlines()] # expand left/right
t.insert(0,'.'*len(t[0])); t.append('.'*len(t[0])) # and top/bottom

def test(i,j,t):
  "was simple boolean result; modified to return coords and char for part2"
  for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
    c = t[i+di][j+dj]
    if not c.isdigit() and c!='.':
      return i+di,j+dj,c
  return i,j,''

r = [] # result part 1
p = [] # result part 2
f = {} # found gears, or rather first number of it (i,j)->n
for i,s in enumerate(t):
  n = False # flag 'in number'
  g = False # good, i.e. adjacent, for part 1
  k = None # coords of adjacent star, for part 2
  for j,c in enumerate(s):
    if c.isdigit():
      if not n:
        n = True
        v = 0 # value
      v = v*10+int(c)
      x,y,z = test(i,j,t)
      if z:
        g = True
        if z=='*':
          k = (x,y)
    else:
      if n:
        if g:
          r.append(v)
          g = False
          if k:
            if k in f:
              p.append(f[k]*v)
            else:
              f[k]=v
          k = None
        n = False
print(sum(r))
print(sum(p))
