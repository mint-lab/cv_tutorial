import cv2 as cv
import numpy as np

def equalizeHist(gray_img):
    if gray_img is None or gray_img.ndim != 2:
        raise ValueError("Input must be a grayscale image (2D array).")

    # 1) Generate the histogram (256 bins for uint8)
    hist = np.bincount(gray_img.ravel(), minlength=256)

    # 2) Generate the CDF (cumulative distribution function)
    cdf = hist.cumsum()

    # 3) Normalize CDF to [0, 255] and make it as a lookup table (LUT)
    lut = np.round(cdf / cdf[-1] * 255)
    lut = np.clip(lut, 0, 255).astype(np.uint8)

    # 4) Map original pixels through LUT
    equalized = lut[gray_img]
    return equalized

if __name__ == "__main__":
    # Read the given image as gray scale
    img = cv.imread('../data/baboon.tif', cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image'

    # Apply histogram equalization
    img_tran = equalizeHist(img)

    # Show all images
    cv.imshow("Original", img)
    cv.imshow("Histogram Equalization (Manual)", img_tran)
    cv.waitKey(0)
    cv.destroyAllWindows()