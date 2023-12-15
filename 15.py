    t = open("15.dat","rt").read().strip().split(',')

    def h(s):
      r=0
      for c in s:
        r=17*(r+ord(c))%256
      return r

    print(sum(h(p) for p in t)) # 512797

    m = [{} for i in range(256)]

    for p in t:
      if p[-1]=='-':
        b = h(p[:-1])
        if p[:-1] in m[b]: del m[b][p[:-1]] # remove
      else:
        k,v = p.split("=") # add
        m[h(k)][k]=int(v) # there or not it's the same op

    s = 0
    for i,b in enumerate(m):
      for j,(k,v) in enumerate(b.items()): # ok even if b is empty
        s += (i+1)*(j+1)*v
    print(s) # 262454
