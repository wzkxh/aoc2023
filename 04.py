    p=0 # point counter, part 1
    q={} # card counter, part 2
    for l in open("04.dat","rt").readlines():
      a,b=l.split(":")
      c=int(a[5:])
      x,y=b.split("|")
      x=set(int(e.strip()) for e in x.split())
      y=[int(e.strip()) for e in y.split()]
      n=sum(e in x for e in y)
      k=q[c]=q.get(c,0)+1
      if n:
        p+=2**(n-1)
        for i in range(c+1,n+c+1):
          q[i]=q.get(i,0)+k
    print(p,sum(q.values()))


