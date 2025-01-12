# Object Detection Using YOLOv5 

## Project Overview

This project implements real-time object detection using the **YOLOv5 (You Only Look Once)** model. The goal is to capture video feed from a camera, detect various objects in real-time, and display the results on the screen. Additionally, the project allows saving the processed video with detected objects in the specified video file format.

---

## Technologies Used:

- **Python**: Programming language used for this project.
- **YOLOv5**: A popular deep learning model for object detection.
- **OpenCV**: Used for video capture, frame processing, and displaying the results.
- **PyTorch**: A deep learning framework used to load the YOLOv5 model.

---

## How the Project Works:

### Real-time Object Detection:
1. The camera feed is captured using OpenCV’s `VideoCapture()`.
2. Each frame is passed to the YOLOv5 model for object detection.
3. Detected objects are annotated with bounding boxes and labels.
4. The model runs on the YOLOv5s variant, which is a smaller, faster model that can be run in real-time on typical hardware.

### Bounding Boxes and Labels:
- YOLOv5 detects objects in the frame and draws bounding boxes around them.
- The object name and confidence score are displayed alongside the bounding box.
- The project supports detecting a wide range of objects, such as people, chairs, bottles, and more.

### Saving the Output:
- The output with object annotations can be saved to a video file (`project_output.avi`) using OpenCV's `VideoWriter()`.
- The video can be played back later for review.

### Exiting the Program:
- Press **q** to quit the application and stop the webcam feed.

---

## Installation

To run this project, Python needs to be installed along with the required libraries. Here’s how to set up the environment:

1. **Install Python**: Ensure Python 3.x is installed on the system.
2. **Install Required Libraries**: Run the following command to install the necessary libraries:

   ```bash
   pip install torch opencv-python
3. **Download the YOLOv5 Model**: The model is loaded dynamically using the `torch.hub.load()` function, so no manual download is required.

---

## How to Run the Code

1. Clone the repository or download the project files.
2. Run the script `object_detection.py`:

   ```bash
   python object_detection.py
3. The camera window will open, and the object detection process will begin.
4. Press q to exit the camera feed.
5. The output video will be saved as project_output.avi.

---
Exmaple Video of Project
Watch a demonstration of the project here:
[Example Project Video](https://drive.google.com/file/d/1UX8bVph9VYbD-VCYGk6-7LlR_tXj8vrK/view?usp=drive_link)
