import cv2 as cv
import numpy as np

# Define morphological operations and kernels
morph_operations = [
    {'name': 'Erode',     'operation': cv.MORPH_ERODE},  # Alternative) cv.erode()
    {'name': 'Dilate',    'operation': cv.MORPH_DILATE}, # Alternative) cv.dilate()
    {'name': 'Open',      'operation': cv.MORPH_OPEN},
    {'name': 'Close',     'operation': cv.MORPH_CLOSE},
    {'name': 'Gradient',  'operation': cv.MORPH_GRADIENT},
    {'name': 'Tophat',    'operation': cv.MORPH_TOPHAT},
    {'name': 'Blackhat',  'operation': cv.MORPH_BLACKHAT},
    {'name': 'Hitmiss',   'operation': cv.MORPH_HITMISS},
]

kernel_tables = [
    {'name': '3x3 Box',   'kenerl': np.ones((3, 3), dtype=np.uint8)},
    {'name': '5x5 Box',   'kenerl': np.ones((5, 5), dtype=np.uint8)},
    {'name': '5x1 Bar',   'kernel': np.ones((5, 1), dtype=np.uint8)},
    {'name': '1x5 Bar',   'kernel': np.ones((1, 5), dtype=np.uint8)},
    {'name': '5x5 Cross', 'kernel': np.array([[0,0,1,0,0], [0,0,1,0,0], [1,1,1,1,1], [0,0,1,0,0], [0,0,1,0,0]], dtype=np.uint8)},
]

# Read the given image as gray scale
img = cv.imread('../data/face.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# Initialize a control parameter
morph_select = 0
kernel_select = 0
n_iterations = 1

while True:
    # Apply morphological operation to the image with the given 'kernel'
    m_name, operation = morph_operations[morph_select].values() # Make alias
    k_name, kernel = kernel_tables[kernel_select].values()      # Make alias
    result = cv.morphologyEx(img, operation, kernel, iterations=n_iterations)

    # Show the image and its filtered result
    info = f'{m_name}({n_iterations}) with {k_name}'
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
    merge = np.hstack((img, result))
    cv.imshow('Morphological Operation: Original | Result', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        morph_select = (morph_select + 1) % len(morph_operations)
    elif key == ord('-') or key == ord('_'):
        morph_select = (morph_select - 1) % len(morph_operations)
    elif key == ord(']') or key == ord('}'):
        kernel_select = (kernel_select + 1) % len(kernel_tables)
    elif key == ord('[') or key == ord('{'):
        kernel_select = (kernel_select - 1) % len(kernel_tables)
    elif key == ord(')') or key == ord('0'):
        n_iterations += 1
    elif key == ord('(') or key == ord('9'):
        n_iterations = max(n_iterations - 1, 1)

cv.destroyAllWindows()
