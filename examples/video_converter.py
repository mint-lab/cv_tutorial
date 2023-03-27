import cv2 as cv

video_file = '../data/PETS09-S2L1-raw.webm'
target_format = 'avi'
target_fourcc = 'XVID' # Note) FourCC: https://learn.microsoft.com/en-us/windows/win32/medfound/video-fourccs

# Read the given video file
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given video, ' + video_file

target = cv.VideoWriter()
while True:
    # Get an image from 'video'
    valid, img = video.read()
    if not valid:
        break

    if not target.isOpened():
        # Open the target video file
        target_file = video_file[:video_file.rfind('.')] + '.' + target_format
        fps = video.get(cv.CAP_PROP_FPS)
        h, w, *_ = img.shape
        is_color = (img.ndim > 2) and (img.shape[2] > 1)
        target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)
        assert target.isOpened(), 'Cannot open the given video, ' + target_file + '.'

    # Add the image to 'target'
    target.write(img)

target.release()
