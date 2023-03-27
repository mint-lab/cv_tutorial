import cv2 as cv
import numpy as np

# Define kernels
kernel_table = [
    {'name': 'Box 3x3',         'kernel': np.ones((3, 3)) / 9},   # Alternative: cv.boxFilter(), cv.blur()
    {'name': 'Gaussian 3x3',    'kernel': np.array([[1, 2, 1],    # Alternative: cv.GaussianBlur()
                                                    [2, 4, 2],
                                                    [1, 2, 1]]) / 16},
    {'name': 'Box 5x5',         'kernel': np.ones((5, 5)) / 25},
    {'name': 'Gaussian 5x5',    'kernel': np.array([[1,  4,  6,  4, 1],
                                                    [4, 16, 24, 16, 4],
                                                    [6, 24, 36, 24, 6],
                                                    [4, 16, 24, 16, 4],
                                                    [1,  4,  6,  4, 1]]) / 256},
    {'name': 'Gradient X',      'kernel': np.array([[-1,  1]])},
    {'name': 'Robert DownRight','kernel': np.array([[-1,  0],
                                                    [ 0,  1]])},
    {'name': 'Prewitt X',       'kernel': np.array([[-1,  0,  1],
                                                    [-1,  0,  1],
                                                    [-1,  0,  1]])},
    {'name': 'Sobel X',         'kernel': np.array([[-1,  0,  1], # Alternative: Sobel()
                                                    [-2,  0,  2],
                                                    [-1,  0,  1]])},
    {'name': 'Scharr X',        'kernel': np.array([[-3,  0,  3], # Alternative: Scharr()
                                                    [-10, 0, 10],
                                                    [-3,  0,  3]])},
    {'name': 'Gradient Y',      'kernel': np.array([[-1], [1]])},
    {'name': 'Robert UpRight',  'kernel': np.array([[ 0,  1],
                                                    [-1,  0]])},
    {'name': 'Prewitt Y',       'kernel': np.array([[-1, -1, -1],
                                                    [ 0,  0,  0],
                                                    [ 1,  1,  1]])},
    {'name': 'Sobel Y',         'kernel': np.array([[-1, -2, -1],
                                                    [ 0,  0,  0],
                                                    [ 1,  2,  1]])},
    {'name': 'Scharr Y',        'kernel': np.array([[-3,-10, -3],
                                                    [ 0,  0,  0],
                                                    [ 3, 10,  3]])},
    {'name': 'Laplacian (4)',   'kernel': np.array([[ 0, -1,  0], # Alternative: Laplacian
                                                    [-1,  4, -1],
                                                    [ 0, -1,  0]])},
    {'name': 'Laplacian (8)',   'kernel': np.array([[-1, -1, -1],
                                                    [-1,  8, -1],
                                                    [-1, -1, -1]])},
    {'name': 'Sharpen (5)',     'kernel': np.array([[ 0, -1,  0],
                                                    [-1,  5, -1],
                                                    [ 0, -1,  0]])},
    {'name': 'Sharpen (9)',     'kernel': np.array([[-1, -1, -1],
                                                    [-1,  9, -1],
                                                    [-1, -1, -1]])},
    {'name': 'Emboss (0)',      'kernel': np.array([[-2, -1,  0],
                                                    [-1,  0,  1],
                                                    [ 0,  1,  2]])},
    {'name': 'Emboss (1)',      'kernel': np.array([[-2, -1,  0],
                                                    [-1,  1,  1],
                                                    [ 0,  1,  2]])},
]

img_list = [
    '../data/lena.tif',
    '../data/baboon.tif',
    '../data/peppers.tif',
    '../data/black_circle.png',
    '../data/salt_and_pepper.png',
    '../data/sudoku.png',
]

# Initialize control parameters
kernel_select = 0
img_select = 0

while True:
    # Read the given image as gray scale
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # Apply convolution to the image with the given 'kernel'
    name, kernel = kernel_table[kernel_select].values() # Make (short) alias
    # result = cv.filter2D(img, -1, kernel)             # Note) dtype: np.uint8 (range: [0, 255]; Be careful!)
    result = cv.filter2D(img, cv.CV_64F, kernel)        # Note) dtype: np.float64
    result = cv.convertScaleAbs(result)                 # Convert 'np.float64' to 'np.uint8' with saturation

    # Show the image and its filtered result
    cv.putText(result, name, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
    cv.putText(result, name, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
    merge = np.hstack((img, result))
    cv.imshow('Image Filtering: Original | Filtered', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        kernel_select = (kernel_select + 1) % len(kernel_table)
    elif key == ord('-') or key == ord('_'):
        kernel_select = (kernel_select - 1) % len(kernel_table)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
