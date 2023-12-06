s = [] # seeds
m = [] # maps 1-7 (start, end (exclusive), destination)
p = 0 # phase of parsing
for l in open("05.dat","rt"):
  l=l.strip()
  if len(l)==0: continue
  if l[0].isalpha():
    p+=1
    if p==1:
      s = [int(x) for x in l[l.find(':')+1:].split()]
    else:
      m.append([])
  else:
    dr,sr,n=[int(x) for x in l.split()]
    m[-1].append((sr,sr+n,dr)); m[-1].sort()

def trace(x): # trace seed through all the maps
  for p in range(len(m)):
    for s,e,d in m[p]:
      if s<=x<e:
        x=d+(x-s); break
  return x

print(min(trace(x) for x in s))

depth = len(m)

def range_trace(x1,x2,l): # recursively trace seed through the map at level l
  if l==depth: return x1
  for r1,r2,d in m[l]:
    if x1<r1:
      if x2<r1: return x1
      return min(x1,range_trace(r1,x2,l))
    if x1<r2:
      if x2<r2: return range_trace(d+(x1-r1),d+(x2-r1),l+1)
      if x2==r2: return range_trace(d+(x1-r1),d+(r2-r1),l+1)
      return min(range_trace(d+(x1-r1),d+(r2-r1),l+1), range_trace(r2,x2,l))
  return range_trace(x1,x2,l+1)

print(min(range_trace(s[i],s[i]+s[i+1],0) for i in range(0,len(s),2)))
