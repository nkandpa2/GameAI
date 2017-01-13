# Program to train the function for shooting

import win32api, win32con
import time
import pyscreenshot as ImageGrab
import threading
import cv2
import numpy as np
import win32gui
import win32ui


#Make this where the blue botton is at the bottom
blueXPos=600
blueYPos=600

def startGame():

    #Click through the login screens
    time.sleep(3)
    click(blueXPos,blueYPos)
    print("Click 1")
    time.sleep(4)
    click(blueXPos,blueYPos)
    print("Click 2")
    time.sleep(5)
    click(blueXPos,blueYPos)
    print("Click 3")
    
#Click funtion for a click press  
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#Click and hold function
def clickTime(x,y,myTime):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(myTime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


#Fire Arrow with pull time 
def fireArrow(pullTime):

    clickTime(blueXPos,blueYPos,pullTime)


#Uses a 2D convolution on the image to find the arrowhead location, and records it
def calculateArrowPos(im):
	
	method = cv2.TM_SQDIFF

	# Read the images from the file
	small_image = cv2.imread('arrow.png',0)
	#result = cv2.matchTemplate(small_image, im, method)
	#mn,mx,mnLoc,mxLoc = cv2.minMaxLoc(result)
	#MPx,MPy = mnLoc

	#use arrow tail instead
	small_image = cv2.imread('tail.png',0)
	#result = cv2.matchTemplate(small_image, im, method)
	#mn,mx,mnLoc,mxLoc = cv2.minMaxLoc(result)
	#MPx,MPy = mnLoc
        cv2.imwrite('img'+str(x)+'.jpg', im) 
        print("Thread done")
	#Save to CSV

	######### DO I NEED TO WORRY ABOUT THE THREADS GETTING OUT OF ORDER AND SAVING WRONG ORDER IN CSV

if __name__ == '__main__':
    startGame()

    pullTime = 1

    fireArrow(pullTime)

    #grab the part of the screen where the arrow is
    ##Note: I had to tune this manually by looking at my screen resolution
    ##Resolution was 2560 x 1440 so I took the middle half of the screen in x direction (1/4*2560 to 3/4*2560)
    ##and bottom half of the screen in y direction
    top = 720 
    left = 640
    height = 720
    width = 1280

    t1 = time.time()
    for x in range(0,15):
        t2 = time.time()
        print(t2 - t1)
        hwin = win32gui.GetDesktopWindow()
        hwindc = win32gui.GetWindowDC(hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
        bmp.SaveBitmapFile(memdc, 'screenshot' + str(x) + '.bmp')
        t2 = time.time()
