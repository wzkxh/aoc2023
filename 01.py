t = open("01.dat","rt").read()

def f(s):
  for c in s:
    if c.isdigit():
      return c

print(sum(int(f(s)+f(s[::-1]))for s in t.splitlines()))

D = {"one":1,"1":1,"two":2,"2":2,"three":3,"3":3,"four":4,"4":4,"five":5,"5":5,
     "six":6,"6":6,"seven":7,"7":7,"eight":8,"8":8,"nine":9,"9":9}

def g(s,rev=False):
  p,r = 999,0
  for n,v in D.items():
    if rev: n=n[::-1]
    k = s.find(n)
    if k<0: continue
    if k<p: p,r=k,v
  return r

print(sum(g(s)*10+g(s[::-1],True)for s in t.splitlines()))

