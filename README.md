## Computer Vision Tutorial

_Computer Vision Tutorial_ includes classical theories and techniques and also recent ML/DL-based methods for computer vision. As classical theories and techniques, the tutorial contains image processing, camera projection models, camera calibration, and pose estimation. As recent ML/DL-based methods, the tutorial deals with object categorization (and backbone networks), and its extensions such as object detection and instance segmentation. It also explains about further topics such as multi-object tracking, structure-from-motion, NeRF, and so on.

This tutorial contains code examples briefly written in [Python](https://python.org/) with [OpenCV](https://opencv.org/) and [PyTorch](https://pytorch.org/).
* :bulb: Some of codes will help readers to understand inside of algorithms (e.g. how it works).
* :wrench: The others of codes will provide usages and applications of OpenCV functions (e.g. how to use it).



### Code Examples
1. **Introduction** (Slides)
2. **Image Editing: Learning OpenCV** (Slides)
	* OpenCV Image Representation
     * Image creation: [image_creation.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_creation.py) :bulb:
   * OpenCV Image and Video Input/Output
     * Image file viewer: [image_viewer.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_viewer.py) :wrench:
     * Image format converter: [image_converter.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_converter.py) :wrench:
     * Video file player: [video_player.py](https://github.com/mint-lab/cv_tutorial/blob/master/video_player.py) :wrench:
     * Video format converter: [video_converter.py](https://github.com/mint-lab/cv_tutorial/blob/master/video_converter.py) :wrench:
   * OpenCV Drawing Functions
     * Shape drawing: [shape_drawing.py](https://github.com/mint-lab/cv_tutorial/blob/master/shape_drawing.py) :wrench:
   * OpenCV High-level GUI
     * (Handling keyboard events) Video file player with frame-based navigation: [video_player+navigation.py](https://github.com/mint-lab/cv_tutorial/blob/master/video_player%2Bnavigation.py) :wrench:
     * (Handling mouse events) Free drawing: [free_drawing.py](https://github.com/mint-lab/cv_tutorial/blob/master/free_drawing.py) :wrench:
   * Image Editing
     * Negative image and flip: [negative_image_and_flip.py](https://github.com/mint-lab/cv_tutorial/blob/master/negative_image_and_flip.py) :bulb:
     * Intensity transformation with contrast and brightness: [intensity_transformation.py](https://github.com/mint-lab/cv_tutorial/blob/master/intensity_transformation.py) :bulb:
     * (Image addition) Alpha blending: [alpha_blending.py](https://github.com/mint-lab/cv_tutorial/blob/master/alpha_blending.py) :bulb:
     * (Image subtraction) Image difference: [image_difference.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_difference.py) :bulb:
     * (Image crop) Image file viewer with the zoom window: [image_viewer+zoom.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_viewer%2Bzoom.py) :bulb:
     * Image resize with backward value copy: [image_resize.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_resize.py) :bulb:
     * Image rotation with backward/forward value copy: [image_rotation.py](https://github.com/mint-lab/cv_tutorial/blob/master/image_rotation.py) :bulb:
   
3. **Image Processing**

4. **Image Formation**

5. **Image Features**

6. **Image Geometry**

7. **Object Recognition**

8. **Object Tracking**

9. **Advanced Topics**



### Authors
* [Sunglok Choi](https://github.com/sunglok)



### Acknowledgements
:information_source: This tutorial has been initiated and maintained to teach undergraduate students in [SEOULTECH](https://en.seoultech.ac.kr/) as the course of _Computer Vision_ (109079).

The authors thank the following contributors and projects.

* [ImageProcessingPlace.com](https://www.imageprocessingplace.com/root_files_V3/image_databases.htm) for test images (pepper, mandril, and lena)
* [MOTChallenge](https://motchallenge.net/vis/PETS09-S2L1) for test images (PETS09-S2L1)