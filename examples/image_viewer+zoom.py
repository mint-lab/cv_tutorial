import cv2 as cv

def mouse_event_handler(event, x, y, flags, param):
    # Catch the mouse position when it moves
    if event == cv.EVENT_MOUSEMOVE:
        param[0] = x # Note) Please do not use 'param = [x, y]'
        param[1] = y

def image_viewer(img_file, zoom_level=10, zoom_box_radius=5, zoom_box_margin=10):
    # Read the given image file
    img = cv.imread(img_file)
    if img is None:
        return False
    img_height, img_width, *_ = img.shape

    # Instantiate a window and register the mouse callback function
    cv.namedWindow('Image Viewer')
    mouse_xy = [-1, -1]
    cv.setMouseCallback('Image Viewer', mouse_event_handler, mouse_xy)

    while True:
        # Paste 'zoom_box' on 'img_copy'
        img_copy = img.copy()
        if mouse_xy[0] >= zoom_box_radius and mouse_xy[0] < (img_width  - zoom_box_radius) and \
           mouse_xy[1] >= zoom_box_radius and mouse_xy[1] < (img_height - zoom_box_radius):
            # Crop the target region
            img_crop = img[mouse_xy[1]-zoom_box_radius:mouse_xy[1]+zoom_box_radius, \
                           mouse_xy[0]-zoom_box_radius:mouse_xy[0]+zoom_box_radius, :]

            # Get the zoomed (resized) image
            zoom_box = cv.resize(img_crop, None, None, zoom_level, zoom_level)

            # Paste the zoomed image on 'img_copy'
            s = zoom_box_margin
            e = zoom_box_margin + len(zoom_box)
            img_copy[s:e,s:e,:] = zoom_box

        # Show the image with the zoom
        cv.imshow('Image Viewer', img_copy)
        key = cv.waitKey(10)
        if key == 27: # ESC
            break

    cv.destroyAllWindows()
    return True



if __name__ == '__main__':
    img_file = '../data/peppers.tif'

    if not image_viewer(img_file):
        print(f'Cannot open the given file, {img_file}')
