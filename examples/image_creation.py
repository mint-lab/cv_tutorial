import numpy as np
import cv2 as cv

img_gray = np.full((480, 640), 255, dtype=np.uint8) # Create a gray image (white)
img_gray[140:240, 220:420] = 0                      # Draw the black box
img_gray[240:340, 220:420] = 127                    # Draw the gray box

img_color = np.zeros((480, 640, 3), dtype=np.uint8) # Create a color image (black)
img_color[:] = 255                                  # Make the color image white
img_color[140:240, 220:420, :] = (0, 0, 255)        # Draw the red box
img_color[240:340, 220:420, :] = (255, 0, 0)        # Draw the blue box

cv.imshow('Gray Image',  img_gray)  # Show 'img_gray'  on a new window named as 'Gray Image'
cv.imshow('Color Image', img_color) # Show 'img_color' on a new window named as 'Color Image'
cv.waitKey()                        # Wait until a user press any key
cv.destroyAllWindows()              # It is necessary only for Spyder IDE.
