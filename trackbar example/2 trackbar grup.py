from  os.path import abspath  
from sys import path
path.insert(0, abspath(__file__).rpartition('\\')[0].rpartition('\\')[0])

if __name__ == '__main__':
  from TRACKBAR import *
  import cv2 as cv     
  window_name = 'tb'
  n = 8
  track_names  = [str(i) for i in range(n)]
  values = [100 for i in range(n)]
  limit = (0,255)  

  cv.namedWindow(window_name, cv.WINDOW_GUI_EXPANDED) 
  gen_trackbar_grup(values, track_names, window_name, limit)

  while True:
      print( values )
      k = cv.waitKey(1) & 0xFF
      if k == 27: break
  cv.destroyAllWindows()
