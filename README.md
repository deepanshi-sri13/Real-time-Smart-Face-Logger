# Real-time Smart Face Logger

This project implements a real-time face recognition system that logs the recognized faces with timestamps into a CSV file. The project uses `face_recognition` and `OpenCV` libraries to identify and track faces from a video feed (via webcam), then records the name of the person and the time they were recognized.

## Features

- Real-time face detection and recognition.
- Logs recognized faces with their name and the current time.
- Automatically creates and appends to a CSV file, with the filename based on the recognized person’s name and the current date.
- Enlarged frame for improved face detection.
- Simple and intuitive interface with bounding boxes and labels for recognized faces.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- `opencv-python`
- `numpy`
- `face-recognition` (This library requires `dlib` to be installed. Refer to the [face_recognition](https://github.com/ageitgey/face_recognition) installation guide for detailed steps.)

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies by running:

   ```bash
   pip install opencv-python numpy face-recognition
