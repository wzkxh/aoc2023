lines = open("02.dat","rt").readlines()

def calc(line,rm,gm,bm):
  rgb={'r':0,'g':0,'b':0}
  head,tail = line.split(":")
  for cubes in tail.split(";"):
    for cube in cubes.split(","):
      n,color = cube.split()
      rgb[color[0]]=max(rgb[color[0]],int(n))
  power = rgb['r']*rgb['g']*rgb['b']
  if rgb['r']<=rm and rgb['g']<=gm and rgb['b']<=bm:
    power += int(head[5:])*1000000
  return power

print(divmod(sum(calc(line,12,13,14)for line in lines),1000000))
