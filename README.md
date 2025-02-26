# Face Detection Project

This repository contains various face detection techniques implemented using OpenCV and dlib.

## Contents

This project includes different approaches for face detection:

1. **HOG-based Face Detection**

   - `face_rec_hog_pic.py`: Detects faces in an image using dlib's HOG-based face detector.
   - `face_rec_hog_video.py`: Detects faces in a video stream using dlib's HOG-based face detector.

2. **CNN-based Face Detection**

   - `face_rec_cnn_pic.py`: Detects faces in an image using dlib's CNN-based face detector.
   - `face_rec_cnn_video.py`: Detects faces in a video stream using dlib's CNN-based face detector.

3. **Haar Cascade Face Detection**

   - `haar_cascade_pic.py`: Detects faces in an image using OpenCV's Haar cascade classifier.
   - `haar_cascade_video.py`: Detects faces in a video stream using OpenCV's Haar cascade classifier.

## Requirements

Before running the scripts, install the necessary dependencies:

```bash
pip install numpy opencv-python dlib
```

Additionally, download the required models:

- [mmod\_human\_face\_detector.dat](http://dlib.net/files/mmod_human_face_detector.dat.bz2) (for CNN-based detection)
- [haarcascade\_frontalface\_default.xml](https://github.com/opencv/opencv/tree/master/data/haarcascades) (for Haar cascade detection)

## Usage

### HOG-based Face Detection

#### For images:

```bash
python face_rec_hog_pic.py
```

Modify the image path in the script before running:

```python
image = cv2.imread('/your image path')
```

#### For videos:

```bash
python face_rec_hog_video.py
```

### CNN-based Face Detection

#### For images:

```bash
python face_rec_cnn_pic.py
```

Modify the image path in the script before running:

```python
image = cv2.imread('/your image path')
```

#### For videos:

```bash
python face_rec_cnn_video.py
```

### Haar Cascade Face Detection

#### For images:

```bash
python haar_cascade_pic.py
```

Modify the image path in the script before running:

```python
img = cv2.imread('/your image path')
```

#### For videos:

```bash
python haar_cascade_video.py
```

## Output

- The scripts will display detected faces with bounding boxes on the image or video feed.

## License

This project is licensed under the MIT License.

