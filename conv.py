import cv2
import numpy as np

method = cv2.TM_SQDIFF

# Read the images from the file

small_image = cv2.imread('head.jpg',0)
large_image = cv2.imread('large_image.jpg',0)


result = cv2.matchTemplate(small_image, large_image, method)
# We want the minimum squared difference
mn,mx,mnLoc,mxLoc = cv2.minMaxLoc(result)


# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc
print(MPy)

#Ranges determine the size of the box above dude's head that we want to search
x_range = 80 
y_range = 80 

patch = large_image[MPy-y_range:MPy, MPx:MPx+x_range]
cv2.imshow('Patch',patch)
cv2.waitKey(0)
cv2.destroyAllWindows()

detector = cv2.SimpleBlobDetector_create()
params = cv2.SimpleBlobDetector_Params()
params.blobColor = 255
params.filterByColor = True
blobs = detector.detect(patch)
print(blobs)

edges = cv2.Canny(patch, 100, 200)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges = (edges == 255)
maxY = 0

for y in range(0,y_range):
    if(np.sum(edges[y,:]) > 0):
       maxY = y_range - y
       break

center_y = (MPy + (MPy - maxY))/2
print(center_y)
