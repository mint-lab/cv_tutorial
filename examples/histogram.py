import numpy as np
import cv2 as cv

def get_histogram(gray_img): # Alternative) cv.calcHist()
    # Assume a gray input image
    # Fix the bin range [0, 256) and bin size 256
    hist = np.zeros((256), dtype=np.uint32)
    for val in range(0, 256):
        hist[val] = sum(sum(gray_img == val)) # Count the occurence in 2D
    return hist

def conv_hist2img(hist):
    img = np.full((256, 256), 255, dtype=np.uint8)
    max_freq = max(hist)
    for val in range(len(hist)):
        normalized_freq = int(hist[val] / max_freq * 255)
        img[0:normalized_freq, val] = 0 # Mark as black
    return img[::-1,:]



if __name__ == '__main__':
    # Read the given image as gray scale
    img = cv.imread('../data/baboon.tif', cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image'

    # Get its histogram
    hist = get_histogram(img)
    print(f'* The number of bins: {len(hist)}')
    print(f'* The maximum frequency: {max(hist)}')
    print(f'* The minimum frequency: {min(hist)}')

    # Show the image and its histogram
    img_hist = conv_hist2img(hist)
    img_hist = cv.resize(img_hist, (len(img[0]), len(img_hist))) # Note) Be careful at (width, height)
    merge = np.vstack((img, img_hist))
    cv.imshow('Histogram: Image | Histogram', merge)
    cv.waitKey()
    cv.destroyAllWindows()
