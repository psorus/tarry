from abc import ABCMeta,abstractmethod





class maze(object):
  """A working class for use in tarry
  def tovalue(s)->"value":
  def fromvalue(s,v)->"maze":
  def motions(s)->"[values]":
  def iswon(s)->bool:
  def copy(s)->"maze":

  
  """
  
  __metaclass__=ABCMeta


  def __init__(s):
    pass


  @abstractmethod
  def tovalue(s)->"value":
    pass
  @abstractmethod
  def fromvalue(s,v)->"maze":
    pass
  
  @abstractmethod
  def motions(s)->"[values]":
    pass
  
  @abstractmethod
  def iswon(s)->bool:
    pass

  @abstractmethod
  def copy(s)->"maze":
    pass


  
