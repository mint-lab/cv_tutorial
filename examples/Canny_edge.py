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
threshold1 = 500
threshold2 = 1200
aperture_size = 5
img_select = -1

while True:
    # Read the given image
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # Get the Canny edge image
    edge = cv.Canny(img, threshold1, threshold2, apertureSize=aperture_size)

    # Show all images
    info = f'Thresh1: {threshold1}, Thresh2: {threshold2}, KernelSize: {aperture_size}'
    cv.putText(edge, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
    cv.putText(edge, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
    merge = np.hstack((img, edge))
    cv.imshow('Canny Edge: Original | Result', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        threshold1 += 2
    elif key == ord('-') or key == ord('_'):
        threshold1 -= 2
    elif key == ord(']') or key == ord('}'):
        threshold2 += 2
    elif key == ord('[') or key == ord('{'):
        threshold2 -= 2
    elif key == ord('>') or key == ord('.'):
        aperture_size = min(aperture_size + 2, 7)
    elif key == ord('<') or key == ord(','):
        aperture_size = max(aperture_size - 2, 3)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
