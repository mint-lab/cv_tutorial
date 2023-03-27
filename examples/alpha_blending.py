import cv2 as cv
import numpy as np

# Read the given images
img1 = cv.imread('../data/baboon.tif')
img2 = cv.imread('../data/peppers.tif')
assert img1 is not None and img2 is not None, 'Cannot read the given images'

# Initialize a control parameter
alpha = 0.5

while True:
    # Apply alpha blending
    blend = (alpha * img1 + (1 - alpha) * img2).astype(np.uint8) # Alternative) cv.addWeighted()

    # Show all images
    info = f'Alpha: {alpha:.1f}'
    cv.putText(blend, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
    cv.putText(blend, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
    merge = np.hstack((img1, img2, blend))
    cv.imshow('Image Blending: Image1 | Image2 | Blended', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        alpha = min(alpha + 0.1, 1)
    elif key == ord('-') or key == ord('_'):
        alpha = max(alpha - 0.1, 0)

cv.destroyAllWindows()
