from  os.path import abspath  
from sys import path
path.insert(0, abspath(__file__).rpartition('\\')[0].rpartition('\\')[0])

if __name__ == '__main__':
  from TRACKBAR import *
  import cv2 as cv     
  window_name = 'tb'
  limit = (0,255)
  val = [100]       # Пользуемся что у списков постоянный адрес 

  cv.namedWindow(window_name, cv.WINDOW_NORMAL) 
  def act():print('изменение')
  gen_trackbar(val, 0, 'with act', window_name, limit, act)
  gen_trackbar(val, 0, 'simple',   window_name, limit     )

  while True:
      print(val)
      k = cv.waitKey(1) & 0xFF
      if k == 27: break

  cv.destroyAllWindows()