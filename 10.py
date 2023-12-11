m = open("10.dat","rt").read().splitlines()
nr,nc = len(m),len(m[0])

start_r = [r for r in range(nr) if 'S' in m[r]][0]
start_c = m[start_r].find('S')

def find_next_from_start(r,c):
  conn='' # determine first connections, then kind of cell
  if r>0    and m[r-1][c] in '|F7': conn+='T'; rc=(r-1,c) # top
  if r<nr-1 and m[r+1][c] in '|LJ': conn+='B'; rc=(r+1,c) # bottom
  if c>0    and m[r][c-1] in '-LF': conn+='L'; rc=(r,c-1) # left
  if c<nc-1 and m[r][c+1] in '-7J': conn+='R'; rc=(r,c+1) # right
  return rc, {'TB':'|','TL':'J','TR':'L','BL':'7','BR':'F','LR':'-'}[conn]

def find_next(r,c):
  i = '-|LF7J'.index(m[r][c])
  return (r+(0,-1,-1,1,1,-1)[i],c-(i==0)),(r+(i==1),c+(1,0,1,1,-1,-1)[i])

prev,(curr,s_kind) = (start_r,start_c),find_next_from_start(start_r,start_c)
path = set(); path.add(prev)
while curr != (start_r,start_c):
  next1,next2 = find_next(*curr)
  next = (next1,next2)[next1==prev]
  prev,curr = curr,next
  path.add(prev)
print(len(path)//2)

m[start_r] = m[start_r].replace('S',s_kind) # make S a regular cell
k = 0
for r,row in enumerate(m):
  inside=False; started=''
  for c,x in enumerate(row):
    if (r,c) in path:
      if x=='|' or x=='7' and started=='L' or x=='J' and started=='F':
        inside=not inside
      elif x in 'FL':
        started=x
    elif inside:
        k+=1
print(k)
