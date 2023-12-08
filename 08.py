from math import lcm

lines = open("08.dat","rt").read().splitlines()

c = '' # code
d = {} # directions
for l in lines:
  if not c: c = l; continue
  if not l: continue
  d[l[:3]]=(l[7:10],l[12:15])

def run(p):
  n = len(c)
  for k in range(50000):
    p = d[p][c[k%n]=='R']
    if p[2]=='Z': break
  return k+1

print(run('AAA'))

r = 1
for p in d.keys():
  if p.endswith("A"):
    r = lcm(r,run(p))
print(r)
