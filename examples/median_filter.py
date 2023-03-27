import cv2 as cv
import numpy as np

img_list = [
    '../data/lena.tif',
    '../data/baboon.tif',
    '../data/peppers.tif',
    '../data/black_circle.png',
    '../data/salt_and_pepper.png',
    '../data/sudoku.png',
]

# Initialize control parameters
kernel_size = 5
img_select = 4

while True:
    # Read the given image
    img = cv.imread(img_list[img_select])
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # Apply the median filter
    result = cv.medianBlur(img, kernel_size)

    # Show all images
    info = f'KernelSize: {kernel_size}'
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 255, thickness=2)
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 0)
    merge = np.hstack((img, result))
    cv.imshow('Medial Filter: Original | Result', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        kernel_size = kernel_size + 2
    elif key == ord('-') or key == ord('_'):
        kernel_size = max(kernel_size - 2, 3)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
