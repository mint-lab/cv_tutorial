import numpy as np
import cv2 as cv

img = cv.imread('../data/peppers.tif')
assert img is not None, 'Cannot read the given image'

# Convert the BGR image to its HSV image
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Show hue, saturation, and value channels as color images
img_hue = np.dstack((img_hsv[:,:,0],
                     np.full_like(img_hsv[:,:,0], 255),
                     np.full_like(img_hsv[:,:,0], 255)))
img_hue = cv.cvtColor(img_hue, cv.COLOR_HSV2BGR)
img_sat = np.dstack((img_hsv[:,:,1], ) * 3)
img_val = np.dstack((img_hsv[:,:,2], ) * 3)
merge = np.hstack((img, img_hue, img_sat, img_val))
cv.imshow('Color Conversion: Image | Hue | Saturation | Value', merge)
cv.waitKey()
cv.destroyAllWindows()
