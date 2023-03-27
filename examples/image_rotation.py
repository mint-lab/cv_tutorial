import numpy as np
import cv2 as cv

def rotate(img, degree):
    # Prepare the (empty) rotated image
    img_rotate = np.zeros(img.shape, dtype=np.uint8)

    # Prepare the inverse transformation
    c, s = np.cos(np.deg2rad(degree)), np.sin(np.deg2rad(degree))
    R = np.array([[c, -s], [s, c]]).T # Note) Transpose is the inverse.
    h, w, *_ = img.shape
    cx = (w - 1) / 2
    cy = (h - 1) / 2

    # Copy each pixel from the given image
    for ry in range(h):
        for rx in range(w):
            dx, dy = R @ [rx - cx, ry - cy]
            x, y = int(dx + cx + 0.5), int(dy + cy + 0.5) # The nearest pixel
            if x >= 0 and y >= 0 and x < w and y < h:
                img_rotate[ry, rx, :] = img[y, x, :]
    return img_rotate

def rotate_forward(img, degree):
    # Prepare the (empty) rotated image
    img_rotate = np.zeros(img.shape, dtype=np.uint8)

    # Prepare the forward transformation
    c, s = np.cos(np.deg2rad(degree)), np.sin(np.deg2rad(degree))
    R = np.array([[c, -s], [s, c]])
    h, w, *_ = img.shape
    cx = (w - 1) / 2
    cy = (h - 1) / 2

    # Copy each pixel from the given image
    for x in range(h):
        for y in range(w):
            dx, dy = R @ [x - cx, y - cy]
            rx, ry = int(dx + cx + 0.5), int(dy + cy + 0.5) # The nearest pixel
            if rx >= 0 and ry >= 0 and rx < w and ry < h:
                img_rotate[ry, rx, :] = img[y, x, :]
    return img_rotate



if __name__ == '__main__':
    # Read the given image file
    img = cv.imread('../data/peppers.tif')
    assert img is not None, 'Cannot read the given image'

    # Initialize a control parameter
    degree = 0

    while True:
        # Rotate the given image
        # Note) Please try 'rotate_forward()' and observe missing pixels
        img_rotate = rotate(img, degree) # Alternative) cv.rotate() only for 90, 180, and 270
                                         #              cv.warpAffine for more general cases
        # Show the rotated image
        info = f'{degree} [deg]'
        cv.putText(img_rotate, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
        cv.putText(img_rotate, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
        cv.imshow('Image Rotation', img_rotate)

        # Process the key event
        key = cv.waitKey()
        if key == 27: # ESC
            break
        elif key == ord('+') or key == ord('='):
            degree = min(degree + 10, 180)
        elif key == ord('-') or key == ord('_'):
            degree = max(degree - 10, -180)

    cv.destroyAllWindows()
