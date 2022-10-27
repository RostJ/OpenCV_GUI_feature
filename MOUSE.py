import cv2

def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        global mouse_cord
        mouse_cord = (x,y)
    pass
cv2.setMouseCallback(camera_window, mouse_callback)