import cv2 as cv
import numpy as np

# Read the given image
img = cv.imread('../data/peppers.tif')
assert img is not None, 'Cannot read the given image'

# Get its negative image
img_nega = 255 - img                         # Alternative) cv.bitwise_xor()

# Get its vertically flipped image
img_flip = img[::-1,:,:]                     # Alternative) cv.flip()

# Show all images
merge = np.hstack((img, img_nega, img_flip)) # Alternative) cv.hconcat()
cv.imshow('Image Editing: Original | Negative | Flip', merge)
cv.waitKey()
cv.destroyAllWindows()
