import numpy as np
import cv2 as cv

def resize(img, scale):
    # Prepare the (empty) resized image
    img_shape = list(img.shape)
    img_shape[0] = int(img_shape[0] * scale)
    img_shape[1] = int(img_shape[1] * scale)
    img_resize = np.zeros(img_shape, dtype=np.uint8)

    # Copy each pixel from the given image
    for ry in range(img_shape[0]):
        y = ry / scale
        for rx in range(img_shape[1]):
            x = rx / scale
            img_resize[ry, rx, :] = img[int(y+0.5), int(x+0.5), :] # Note) Rounding: int(x+0.5)
    return img_resize



if __name__ == '__main__':
    img_file = '../data/peppers.tif'

    # Read the given image file
    img = cv.imread(img_file)
    assert img is not None, 'Cannot read the given image, ' + img_file

    # Initialize a control parameter
    scale = 1

    while True:
        # Resize the given image
        img_resize = resize(img, scale) # Alternative) cv.resize()

        # Show the resized image
        info = f'x{scale:.1f}'
        cv.putText(img_resize, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
        cv.putText(img_resize, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
        cv.imshow('Image Resize', img_resize)

        # Process the key event
        key = cv.waitKey()
        if key == 27: # ESC
            break
        elif key == ord('+') or key == ord('='):
            scale = min(scale + 0.1, 3)
        elif key == ord('-') or key == ord('_'):
            scale = max(scale - 0.1, 0.3)

    cv.destroyAllWindows()
