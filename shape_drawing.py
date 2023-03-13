import numpy as np
import cv2 as cv

# Prepare a canvas
canvas = np.full((480, 640, 3), 255, dtype=np.uint8)

# Draw lines with its label
cv.line(canvas, ( 10,  10), (630, 470), color=(200, 200, 200), thickness=2)
cv.line(canvas, (630,  10), ( 10, 470), color=(200, 200, 200), thickness=2)
cv.line(canvas, (320,  10), (320, 470), color=(200, 200, 200), thickness=2)
cv.line(canvas, ( 10, 240), (630, 240), color=(200, 200, 200), thickness=2)
cv.putText(canvas, 'Line', (10, 20), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))

# Draw a circle with its label
center = (100, 240) # Note) How about real numbers?
cv.circle(canvas, center, radius=60, color=(0, 0, 255), thickness=5)
cv.putText(canvas, 'Circle', center, cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 0))

# Draw a rectangle with its label
pt1, pt2 = (320-60, 240-50), (320+60, 240+50)
cv.rectangle(canvas, pt1, pt2, color=(0, 255, 0), thickness=-1)
cv.putText(canvas, 'Rectangle', pt1, cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255))

# Draw a polygon (triangle) with its label
pts = np.array([(540, 240-50), (540-55, 240+50), (540+55, 240+50)]) # Note) Why np.array?
cv.polylines(canvas, [pts], True, color=(255, 0, 0), thickness=5)
cv.putText(canvas, 'Polylines', pts[0].flatten(), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 200, 200))

# Show the canvas
cv.imshow('Shape Drawing', canvas)
cv.waitKey()
cv.destroyAllWindows()
