import matplotlib.pyplot as plt
import cv2 as cv

# Read the given image as gray scale
img = cv.imread('../data/baboon.tif', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# Apply histogram equalization
img_tran = cv.equalizeHist(img)

# Derieve the histogram
bin_width = 4 # Note) The value should be the power of 2.
bin_num = int(256 / bin_width)
hist = cv.calcHist([img], [0], None, [bin_num], [0, 255])
hist_tran = cv.calcHist([img_tran], [0], None, [bin_num], [0, 255])

# Show all images and their histograms
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.plot(range(0, 256, bin_width), hist / 1000)
plt.xlabel('Intensity [0, 255]')
plt.ylabel('Frequency (1k)')
plt.subplot(2, 2, 3)
plt.imshow(img_tran, cmap='gray')
plt.axis('off')
plt.subplot(2, 2, 4)
plt.plot(range(0, 256, bin_width), hist_tran / 1000)
plt.xlabel('Intensity [0, 255]')
plt.ylabel('Frequency (1k)')
plt.show()
