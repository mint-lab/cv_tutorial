import cv2 as cv

img_file = '../data/peppers.tif'

# Read the given image file
img = cv.imread(img_file)
assert img is not None, 'Cannot read the given image, ' + img_file

# Show the image
cv.imshow('Image Viewer', img)
cv.waitKey()
cv.destroyAllWindows()
