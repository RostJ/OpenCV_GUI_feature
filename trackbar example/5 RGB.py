from  os.path import abspath  
from sys import path
path.insert(0, abspath(__file__).rpartition('\\')[0].rpartition('\\')[0])

if __name__ == '__main__':
  from TRACKBAR import rgb_trackbar
  from cv2 import waitKey, destroyAllWindows
  val = rgb_trackbar() 
  while True:
      print(val)
      k = waitKey(1) & 0xFF
      if k == 27: break
  destroyAllWindows()