import numpy as np
import cv2 as cv
from Sobel_edge import drawText

# Read the given image as gray scale
img = cv.imread('../data/sudoku.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'
img_threshold_type = cv.THRESH_BINARY_INV # Type: Detect pixels close to 'black' (inverse)

# Initialize control parameters
threshold = 127
adaptive_type = cv.ADAPTIVE_THRESH_MEAN_C
adaptive_blocksize = 99
adaptive_C = 4

while True:
    # Apply thresholding to the image
    _, binary_user = cv.threshold(img, threshold, 255, img_threshold_type)
    threshold_otsu, binary_otsu = cv.threshold(img, threshold, 255, img_threshold_type | cv.THRESH_OTSU)
    binary_adaptive = cv.adaptiveThreshold(img, 255, adaptive_type, img_threshold_type, adaptive_blocksize, adaptive_C)

    # Show the image and its thresholded result
    drawText(binary_user, f'Threshold: {threshold}')
    drawText(binary_otsu, f'Otsu Threshold: {threshold_otsu}')
    adaptive_type_text = 'M' if adaptive_type == cv.ADAPTIVE_THRESH_MEAN_C else 'G'
    drawText(binary_adaptive, f'Type: {adaptive_type_text}, BlockSize: {adaptive_blocksize}, C: {adaptive_C}')
    merge = np.vstack((np.hstack((img, binary_user)),
                       np.hstack((binary_otsu, binary_adaptive))))
    cv.imshow('Thresholding: Original | User | Otsu | Adaptive', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        threshold += 1
    elif key == ord('-') or key == ord('_'):
        threshold -= 1
    elif key == ord('\t'):
        if adaptive_type == cv.ADAPTIVE_THRESH_MEAN_C:
            adaptive_type = cv.ADAPTIVE_THRESH_GAUSSIAN_C
        else:
            adaptive_type = cv.ADAPTIVE_THRESH_MEAN_C
    elif key == ord(']') or key == ord('}'):
        adaptive_blocksize += 2
    elif key == ord('[') or key == ord('{'):
        adaptive_blocksize = max(adaptive_blocksize - 2, 3)
    elif key == ord('>') or key == ord('.'):
        adaptive_C += 1
    elif key == ord('<') or key == ord(','):
        adaptive_C -= 1

cv.destroyAllWindows()
