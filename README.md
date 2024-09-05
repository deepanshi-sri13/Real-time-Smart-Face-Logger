# Real-time Smart Face Logger ![](https://img.shields.io/badge/python-3.8.6-blue.svg)

This project implements a real-time face recognition system that logs the recognized faces with timestamps into a CSV file. The project uses `face_recognition` and `OpenCV` libraries to identify and track faces from a video feed (via webcam), then records the name of the person and the time they were recognized.

## Features

- Real-time face detection and recognition.
- Logs recognized faces with their name and the current time.
- Automatically creates and appends to a CSV file, with the filename based on the recognized person’s name and the current date.
- Enlarged frame for improved face detection.
- Simple and intuitive interface with bounding boxes and labels for recognized faces.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8
- `opencv-python`
- `numpy`
- `face-recognition` (This library requires `dlib` to be installed.)

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies by running:

   ```bash
   pip install opencv-python numpy face-recognition
3. Place the images of the people you want to recognize in the same directory as the code. Update the filenames in the script accordingly.

## Usage

Modify the code to include images of the individuals you'd like to recognize, and update the `known_face_names` and `known_face_encodings` with their corresponding details.

**Example:**

  ```c
  known_face_names = ["deepanshi", "name2"]
  known_face_encodings = [deepanshi_encoding, name2_encoding]
  ```


