d = [e.split() for e in open("07.dat","rt").read().splitlines()]

w = {'55555':7,'44441':6,'33322':5,'33311':4,'22221':3,'22111':2,'11111':1}

def classify(s): return ''.join(sorted((str(s.count(e)) for e in s),reverse=True))
m = {'A':'e','K':'d','Q':'c','J':'b','T':'a'}
o = sorted(((w[classify(a)],''.join(m.get(e,e) for e in a)),int(b)) for a,b in d)
print(sum(i*e[1] for i,e in enumerate(o,1))) # 247823654

def classify2(s):
  if 'J' not in s: return classify(s)
  return max((w[c:=classify2(s.replace('J',v,1))],c) for v in '23456789TQKA')[1]
m2 = {'A':'e','K':'d','Q':'c','J':'1','T':'a'}
o = sorted(((w[classify2(a)],''.join(m2.get(e,e) for e in a)),int(b)) for a,b in d)
print(sum(i*e[1] for i,e in enumerate(o,1))) # 245461700
