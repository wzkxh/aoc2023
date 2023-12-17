import sys
sys.setrecursionlimit(10000)

t = open("16.dat","rt").read().replace("\\","`").splitlines()
nr = len(t)
nc = len(t[0])
p = v = None # sets: path, (direction,(r,c)); visited (r,c)

def f(d,r,c):
  if (d,r,c) in p: return
  if r<0 or c<0 or r>=nr or c>=nc: return
  p.add((d,r,c))
  v.add(10000*r+c)
  match d:
    case 'R':
      match t[r][c]:
        case '.': f(d,r,c+1)
        case '-': f(d,r,c+1)
        case '|': f('U',r-1,c); f('D',r+1,c)
        case '/': f('U',r-1,c)
        case '`': f('D',r+1,c)
    case 'L':
      match t[r][c]:
        case '.': f(d,r,c-1)
        case '-': f(d,r,c-1)
        case '|': f('U',r-1,c); f('D',r+1,c)
        case '/': f('D',r+1,c)
        case '`': f('U',r-1,c)
    case 'D':
      match t[r][c]:
        case '.': f(d,r+1,c)
        case '|': f(d,r+1,c)
        case '-': f('L',r,c-1); f('R',r,c+1)
        case '/': f('L',r,c-1)
        case '`': f('R',r,c+1)
    case 'U':
      match t[r][c]:
        case '.': f(d,r-1,c)
        case '|': f(d,r-1,c)
        case '-': f('L',r,c-1); f('R',r,c+1)
        case '/': f('R',r,c+1)
        case '`': f('L',r,c-1)

def solve(d,r,c):
  global p,v
  p = set()
  v = set()
  f(d,r,c)
  return len(v)

print(solve('R',0,0)) # 8901

x = 0
for r in range(nr):
  x = max(x,solve('R',r,0))
  x = max(x,solve('L',r,nc-1))
for c in range(nc):
  x = max(x,solve('D',0,c))
  x = max(x,solve('U',nr-1,c))
print(x) # 9064
