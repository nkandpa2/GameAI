import cv2
from cv2 import cv

method = cv.CV_TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread('small_image.png')
large_image = cv2.imread('large_image.jpg')

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)


# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

print(MPx)
print(MPy)
