import cv2 as cv
import numpy as np

def drawText(img, text, org=(10, 25), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=0.6, color=(0, 0, 0), colorBoundary=(255, 255, 255)):
    cv.putText(img, text, org, fontFace, fontScale, colorBoundary, thickness=2)
    cv.putText(img, text, org, fontFace, fontScale, color)



if __name__ == '__main__':
    img_list = [
        '../data/lena.tif',
        '../data/baboon.tif',
        '../data/peppers.tif',
        '../data/black_circle.png',
        '../data/salt_and_pepper.png',
        '../data/sudoku.png',
    ]

    # Initialize control parameters
    edge_threshold = 0.1
    img_select = 3

    while True:
        # Read the given image as gray scale
        img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)
        assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

        # Extract edges using two-directional Sobel responses
        #  and normalize their values within [0, 1] (Note: 1020 derived from 255 * (1+2+1))
        dx   = cv.Sobel(img, cv.CV_64F, 1, 0) / 1020 # Sobel x-directional response
        dy   = cv.Sobel(img, cv.CV_64F, 0, 1) / 1020 # Sobel y-directional response
        mag  = np.sqrt(dx*dx + dy*dy) / np.sqrt(2)   # Sobel magnitude
        ori  = np.arctan2(dy, dx)                    # Sobel orientation
        edge = mag > edge_threshold # Alternative) cv.threshold(), cv.adaptiveThreshold()

        # Prepare the orientation image as the BGR color
        ori[ori < 0] = ori[ori < 0] + 2*np.pi        # Convert [-np.pi, np.pi) to [0, 2*np.pi)
        ori_hsv = np.dstack((ori / (2*np.pi) * 180,  # HSV color - Hue channel
                             np.full_like(ori, 255), # HSV color - Saturation channel
                             mag * 255))             # HSV color - Value channel
        ori_bgr = cv.cvtColor(ori_hsv.astype(np.uint8), cv.COLOR_HSV2BGR)

        # Prepare the original, Sobel X/Y, magnitude, and edge images as the BGR color
        img_bgr  = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        dx_bgr   = cv.cvtColor(abs(dx * 255).astype(np.uint8), cv.COLOR_GRAY2BGR)
        dy_bgr   = cv.cvtColor(abs(dy * 255).astype(np.uint8), cv.COLOR_GRAY2BGR)
        mag_bgr  = cv.cvtColor((mag * 255).astype(np.uint8),   cv.COLOR_GRAY2BGR)
        edge_bgr = cv.cvtColor((edge * 255).astype(np.uint8),  cv.COLOR_GRAY2BGR)

        # Show all images
        drawText(img_bgr, 'Original')
        drawText(dx_bgr,  'SobelX')
        drawText(dy_bgr,  'SobelY')
        drawText(mag_bgr, 'Magnitude')
        drawText(ori_bgr, 'Orientation')
        drawText(edge_bgr, f'EdgeThreshold: {edge_threshold:.2f}')
        merge = np.vstack((np.hstack((img_bgr, dx_bgr, dy_bgr)),
                           np.hstack((edge_bgr, mag_bgr, ori_bgr))))
        cv.imshow('Sobel Edge', merge)
        key = cv.waitKey()
        if key == 27: # ESC
            break
        elif key == ord('+') or key == ord('='):
            edge_threshold = min(edge_threshold + 0.02, 1)
        elif key == ord('-') or key == ord('_'):
            edge_threshold = max(edge_threshold - 0.02, 0)
        elif key == ord('\t'):
            img_select = (img_select + 1) % len(img_list)

    cv.destroyAllWindows()
