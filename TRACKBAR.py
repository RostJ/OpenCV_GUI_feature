def gen_trackbar(val = [0], i = 0, t_name = '1',w_name = 'tb', limit = (0,255), action = lambda:None): # Генерация трэкбара с привязкой переменной
  from cv2 import createTrackbar, setTrackbarPos
  if action != None:
    def rec(x):
      val[i] = int(x) # Пользуемся что у списков постоянный адрес и создаём функцию перезаписи которая получает ссылку на исходный список
      action()   # Можем выполнить дополнительное действие при изменении
  else: 
    def rec(x): val[i] = x # Только перезапись
  createTrackbar(t_name,w_name,limit[0],limit[1],rec)   # Создание трэкера
  setTrackbarPos(t_name,w_name,val[i])                  # Задание начального начения
  return val

def gen_trackbar_grup(val:list, t_names = ['min', 'max'], w_name = 'tb', limit = (0,255)): # Генерация трекбаров по списку имён
  for i, t_name in enumerate(t_names):
      gen_trackbar(val, i, t_name, w_name, limit)
  return val
        
def gen_trackbar_grups(val:list, t_names = ['r','g','b'], g_names =['min', 'max'], w_name = 'tb', limit = (0,255)): # Генерация нескольких групп одинаковых трекеров
  for i, g_name in enumerate(g_names):
    names = [t_names[j] + g_name for j in range(len(t_names))]
    gen_trackbar_grup(val[i], names, w_name, limit)
  return val
    
def gen_trackbar_window(val = [0], track_names = 'trackbar', grup_names = '', window_name = 'trackbar',limit = (0,255)): # Генерация окна с трекерами
  from cv2 import namedWindow, WINDOW_NORMAL
  namedWindow(window_name, WINDOW_NORMAL) 
  gen_trackbar_grups(val, track_names, grup_names, window_name, limit)
  return val

def rgb_trackbar(val = None, track_names = None, grup_names = None, window_name = None,limit = None): # Пресет для настройки rgb границ 
  if window_name == None: window_name = 'RGB'
  if track_names == None: track_names = ['R','G','B']
  if grup_names == None:  grup_names  = ['_min','_max']
  if limit == None:       limit       = (0,255)
  if val == None:         val         = [[100,100,100],[100,100,100]] 
  gen_trackbar_window(val, track_names, grup_names, window_name, limit)
  return val # Возврощается список с изменяемыми значениями

def bgr_trackbar(val = None, track_names = None, grup_names = None, window_name = None,limit = None): # Пресет для настройки rgb границ 
  if window_name == None: window_name = 'BGR'
  if track_names == None: track_names = ['B','G','R']
  if grup_names == None:  grup_names  = ['_min','_max']
  if limit == None:       limit       = (0,255)
  if val == None:         val         = [[100,100,100],[100,100,100]] 
  gen_trackbar_window(val, track_names, grup_names, window_name, limit)
  return val # Возврощается список с изменяемыми значениями

def hsv_trackbar(val = None, track_names = None, grup_names = None, window_name = None,limit = None): # Пресет для настройки hsv границ 
  if window_name == None: window_name = 'HSV'
  if track_names == None: track_names = ['H','S','V']
  if grup_names == None:  grup_names  = ['_min','_max']
  if limit == None:       limit       = (0,255)
  if val == None:         val         = [[100,100,100],[100,100,100]] 
  gen_trackbar_window(val, track_names, grup_names, window_name, limit)
  return val # Возврощается список с изменяемыми значениями
  
def grey_trackbar(val = None, track_names = None, window_name = None,limit = None): # Пресет для настройки границ яркости 
  if window_name == None: window_name = 'GREY'
  if track_names == None: track_names = ['MIN','MAX']
  if limit == None:       limit       = (0,255)
  if val == None:         val         = [0,255] 
  from cv2 import namedWindow, WINDOW_NORMAL
  namedWindow(window_name, WINDOW_NORMAL) 
  gen_trackbar_grup(val, track_names,  window_name, limit)
  return val # Возврощается список с изменяемыми значениями
 
def brigh_contrast_trackbar(val = None, track_names = None, window_name = None,limit = None): # Пресет для настройки границ яркости 
  if window_name == None: window_name = 'brigh contrast'
  if track_names == None: track_names = ['brigh','contrast']
  if limit == None:       limit       = ((0,255),(0,10))
  if val == None:         val         = [0,100] 
  from cv2 import namedWindow, WINDOW_NORMAL
  namedWindow(window_name, WINDOW_NORMAL) 
  for i in [0,1]:
    gen_trackbar(val, i, track_names[i],window_name, limit[i])
  return val # Возврощается список с изменяемыми значениями
 