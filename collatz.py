from maze import *



class collatz(maze):
  goal=25
  maxv=100
  def __init__(s,v=1):
    maze.__init__(s)
    s.v=int(v)
  
  def tovalue(s)->"value":
    return s.v
  def fromvalue(s,v)->"maze":
    return collatz(v)
  def motions(s)->"[values]":
    ret=[]
    if s.v%2==0:
      ret.append(int(s.v/2))
    if s.v%3==1:
      ret.append(int((s.v-1)/3))
    if 3*s.v+1<s.maxv:ret.append(3*s.v+1)
    if 2*s.v<s.maxv:ret.append(2*s.v)
    return ret
      
    
  def iswon(s)->bool:
    return s.v==s.goal
  def __repr__(s)->str:
    return str(s)
  def __str__(s)->str:
    return str(s.v)
  def copy(s)->"maze":
    return collatz(s.v)