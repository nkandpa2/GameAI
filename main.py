import win32api, win32con
import time

#Make this where the blue botton is at the bottom
blueXPos=790
blueYPos=725
def startGame():

    #Click through the login screens
    time.sleep(3)
    click(blueXPos,blueYPos)
    print("Click 1")
    time.sleep(2)
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
    time.sleep(3)
    click(blueXPos,blueYPos)

#Runs a 2D convolution on the image to find the object location
def determineObjectLocation():

    #Capture screen image


    #Determine center of image (ideally this will be the "sweet spot")
    xPos=1
    yPos=1
    return (xPos,yPos)

#Uses experimentally determined function for the arrow to calculate
#how long we should click and hold
def determineArrowHoldTime(x,y):
    print("TODO")
    return 1

startGame()

while(True):

    # Run a 2D Convolution to determine X and Y pos 
    (x,y) = determineObjectLocation()

    pullTime = determineArrowHoldTime(x,y)

    fireArrow(pullTime)
            
