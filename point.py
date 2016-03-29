from .. import utils



class Point(object):
  
  def __init__(self, x, y, mark):
      self.x = x
      self.y = y
      self.mark = mark
  
  def check_coincident(self, test):
      return check_coincident((self.x, self.y)), test)
  
  def shift_point(self, self.x, self.y):
      point = utils.shift_point(self.x, self.y)
      self.x = utils.getx(point)
      self.y = utils.gety(point)
