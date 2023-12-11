def expand(g,rc,k):
  last_rc,exp = -1,0
  for gi in g:
    if gi[rc]>last_rc+1:
      exp += (k-1)*(gi[rc]-(last_rc+1))
    last_rc = gi[rc]
    gi[rc] += exp

def solve(g,k):
  for rc in (0,1):
    g.sort(key=lambda x:x[rc])
    expand(g,rc,k)
  d = 0
  for i,gi in enumerate(g):
    for gj in g[i+1:]:
      d += abs(gi[0]-gj[0])+abs(gi[1]-gj[1])
  return d

g = [[r,c] for r,l in enumerate(open("11.dat","rt"))for c,x in enumerate(l)if x=='#']
g_copy = [x[:] for x in g] # we use & modify list or lists, so make deep copy
print(solve(g,2)) # 9681886
print(solve(g_copy,1_000_000)) # 791134099634
