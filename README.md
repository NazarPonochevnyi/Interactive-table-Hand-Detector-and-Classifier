# Interactive-table-Hand-Detector-and-Classifier

![](https://img.shields.io/badge/-status:wip-5319e7.svg)
![](https://img.shields.io/github/license/NazarPonochevnyi/Interactive-table-Hand-Detector-and-Classifier)
![](https://img.shields.io/github/languages/code-size/NazarPonochevnyi/Interactive-table-Hand-Detector-and-Classifier)
![](https://img.shields.io/github/last-commit/NazarPonochevnyi/Interactive-table-Hand-Detector-and-Classifier)

🖐️ Interships 2018 task - Computer Vision | My solution

### HOW TO START

To run my program you need to download Python 3.6
(https://www.python.org/)

1. Open CMD.EXE and install the following modules.

        pip3 install keras
        pip3 install tensorflow
        pip3 install opencv-python
2. Navigate to the directory where you extracted the Solution.zip file.

        cd /d D: (The drive in which you extracted the Solution.zip file)
        cd folder/where/you/extracted/Solution.zip/file
3. Run "find_hands.py" or "find_hands_video.py".

        python3 find_hands.py
      or

        python3 find_hands_video.py

##### The note:
* The first run of the program can be very long, about 1 min 30 seconds. Please be patient.
* If you want to see the code or change INPUT_VARIABLES, open the file using a text editor and read the information in the file header.

### Results of detection and classification

Result of work on image with left hand:

![Result of work on image with left hand](https://github.com/NazarPonochevnyi/Interactive-table-Hand-Detector-and-Classifier/blob/master/z_results/test_left.jpg)

Result of work on image with right hand:

![Result of work on image with right hand](https://github.com/NazarPonochevnyi/Interactive-table-Hand-Detector-and-Classifier/blob/master/z_results/test_right.jpg)

Result of work on image with both hands:

![Result of work on image with both hands](https://github.com/NazarPonochevnyi/Interactive-table-Hand-Detector-and-Classifier/blob/master/z_results/test_both.jpg)

##### About "find_hands.py":
    Find | Detection | Classification hands

    This is a program that opens an image file or directory with image files. Then she
    detect hands and classifies is the left or right hand.
    
    To select the next image in the folder, press any key.

    Default INPUT_VARIABLES:
        INPUT_PATH - './Test189x110/27734/'
        LEFT HAND - RED COLOR
        RIGHT HAND - BLUE COLOR
        BORDER_SIZE - 1 px
        SCALE_IMAGE - scaling 2 times

##### About "find_hands_video.py":
    Find | Detection | Classification hands | On video

    This is the program that opens the video file. Then she detect hands and
    classifies is the left or right hand.
    
    To stop video capture, press ESC.

    Default INPUT_VARIABLES:
        INPUT_PATH - use stream from the built-in camera
        LEFT HAND - RED COLOR
        RIGHT HAND - BLUE COLOR
        BORDER_SIZE - 1 px
        SCALE_IMAGE - no scaling

#### "What did I use?"
* To find the hands on the image - OpenCV HaarCascade (.xml), which was fully trained by me.
* To For recognition of the left and right hand - a simple binary classifier that works with convolutional neural networks. To create the model, the Keras library was used, and on the backend - TensorFlow.

Author: Nazar Ponochevnyi

## License
[MIT License](./LICENSE)
