import cv2 as cv

img_file = 'data/peppers_color.tif'
target_format = 'png'

# Read the given image file
img = cv.imread(img_file)

# Check whether the image is valid or not
if img is not None:
    # Write 'img' as a file named 'target_file'
    target_file = img_file[:img_file.rfind('.')] + '.' + target_format
    cv.imwrite(target_file, img)
