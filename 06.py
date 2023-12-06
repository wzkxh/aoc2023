'''
t = [ 53,  91,  67,  68]
d = [250,1330,1081,1025]
def ways(t,d): return sum((t-v)*v>d for v in range(0,t+1))
p=1
for i in range(len(t)): p*=ways(t[i],d[i])
print(p) #  625968
print(ways(53916768,250133010811025)) # 43663323
'''

import math
t,d=(s.split()[1:] for s in open("06.dat","rt").read().splitlines())
print(math.prod(sum((int(a)-v)*v>int(b) for v in range(0,int(a)+1)) for a,b in zip(t,d)))
p,q=-int(''.join(t)),int(''.join(d))
a,b=-p/2,math.sqrt((p/2)**2-q)
print(math.floor(a+b)-math.ceil(a-b)+1)
