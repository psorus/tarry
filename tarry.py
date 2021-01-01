import random
import math

def mean(q):
  ret=0.0
  for qq in q:
    ret+=qq
  return ret/len(q)
def std(q,m=None):
  if len(q)<2:return 0.0
  if m is None:m=mean(q)
  ret=0.0
  for qq in q:
    ret+=(qq-m)**2
  ret/=len(q)-1
  return math.sqrt(ret)

def timestat(m,solv,n=100):
  st=[]
  for i in range(n):
    ac,steps=solv(m.copy())
    st.append(math.log(steps))
  m=mean(st)
  return m,std(st,m)/math.sqrt(len(st))

def simplesolve(m):
  steps=0
  while not m.iswon():
    # print("being at",m.tovalue(),"having options",m.motions())
    m=m.fromvalue(random.choice(m.motions()))
    # print("!!!!!!!!")
    # print(m)
    # print("!!!!!!!!")
    steps+=1
  return m,steps

def tarry_(m):
  steps=0
  states={}
  revert=None
  while not m.iswon():
    # print("being at",m.tovalue())
    options=m.motions()
    s=[]
    for op in options:
      if op in states.keys():
        s.append(states[op])
      else:
        s.append(0)
    se=list(set(s))
    se.sort()
    ov=m.tovalue()
    states[ov]=1
    # print("setting",ov,"to",1)
    for ss in se:
      posi=[i for i,x in enumerate(s) if x==ss]
      if len(posi)>0:
        # print("updating","(",ss,")",posi)
        m=m.fromvalue(options[random.choice(posi)])
        break
    # if not revert is None:
      # states[revert]=2
      # print("setting",revert,"to",2)
    # revert=ov
    steps+=1
  return m,steps

def tarry(m):
  steps=0
  states={}
  revert=None
  while not m.iswon():
    # print("being at",m.tovalue())
    options=m.motions()
    s=[]
    for op in options:
      if op in states.keys():
        s.append(states[op])
      else:
        s.append(0)
    se=list(set(s))
    se.sort()
    ov=m.tovalue()
    states[ov]=1+steps
    # print("setting",ov,"to",1)
    for ss in se:
      posi=[i for i,x in enumerate(s) if x==ss]
      if len(posi)>0:
        # print("updating","(",ss,")",posi)
        m=m.fromvalue(options[random.choice(posi)])
        break
    # if not revert is None:
      # states[revert]=2
      # print("setting",revert,"to",2)
    # revert=ov
    steps+=1
  return m,steps


