from  os.path import abspath  
from sys import path
path.insert(0, abspath(__file__).rpartition('\\')[0].rpartition('\\')[0])

if __name__ == '__main__':
  from TRACKBAR import *
  import cv2 as cv     
  window_name = 'RGB'
  track_names, grup_names = ['R','G','B'], ['_min','_max']
  limit = (0,255)
  val = [[100,100,100],[100,100,100]] 

  gen_trackbar_window(val, track_names, grup_names, window_name, limit)

  while True:
      print(val)
      k = cv.waitKey(1) & 0xFF
      if k == 27: break

  cv.destroyAllWindows()