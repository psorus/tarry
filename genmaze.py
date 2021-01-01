from maze import *

import random
import math

class arrmaze(maze):
  sx=20
  sy=20
  def __init__(s,q=None,p=None):
    maze.__init__(s)
    if q is None:
      s.gen()
    else:
      s.q=q
    if p is None:
      s.p=s.initpos()
    else:
      s.p=p
   
  def initpos(s):
    return (0,0)
  
  def gen(s)->None:
    """generates a random maze"""
    # s.q=[[random.randint(0,1) for j in range(20)] for i in range(20)]
    s.q=[[1 for j in range(s.sx)] for i in range(s.sy)]
    for i in range(int(math.sqrt(s.sx))):s.assurepassage()
  
  def __repr__(s):
    return str(s)
  
  def modplate(s):
    c=[[zw for zw in ac] for ac in s.q]
    c[s.p[0]][s.p[1]]=2
    return c
  
  def __str__(s):
    return "\n".join([" ".join([str(x) for x in ac]) for ac in s.modplate()])
  
  def assurepassage(s,i=0,j=0,fi=None,fj=None):
    if fi is None:fi=len(s.q)
    if fj is None:fj=len(s.q[0])
    li,lj=fi,fj

    s.q[i][j]=0
    while not (i==li-1 and j==lj-1):
      if random.randint(0,1)==0:
        # i+=random.randint(-1,1)
        i+=1
      else:
        # j+=random.randint(-1,1)
        j+=1
      if i<0:i=0
      if j<0:j=0
      if i>=li:i=li-1
      if j>=lj:j=lj-1
      s.q[i][j]=0
      # print(i,j)
  
  def tovalue(s)->"value":
    return s.p
  def fromvalue(s,v)->"maze":
    return arrmaze(s.q,v)
  def motions(s)->"[values]":
    li,lj=len(s.q),len(s.q[0])
    pi,pj=s.p
    ret=[]
    if pj<lj-1:
      if s.q[pi][pj+1]==0:ret.append((pi,pj+1))
    if pi<li-1:
      if s.q[pi+1][pj]==0:ret.append((pi+1,pj))
    if pj>0:
      if s.q[pi][pj-1]==0:ret.append((pi,pj-1))
    if pi>0:
      if s.q[pi-1][pj]==0:ret.append((pi-1,pj))
      
    return ret
  
  def iswon(s)->bool:
    return s.p[0]==len(s.q)-1 and s.p[1]==len(s.q[0])-1

  def copy(s)->"maze":
    return arrmaze([[zw for zw in ac] for ac in s.q],s.p)

