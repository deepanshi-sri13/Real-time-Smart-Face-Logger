# Real-time Smart Face Logger ![](https://img.shields.io/badge/python-3.8.6-blue.svg)

A Python-based real-time face recognition system that captures video input via webcam, detects faces, and logs the recognized individuals' names and timestamps into a CSV file. This project uses the `face_recognition` and `OpenCV` libraries to perform real-time detection and logging.

## Features

- **Real-time face detection:** Captures frames from the webcam, detects faces, and recognizes them in real-time.
- **Face recognition:** Compares faces in the video feed with pre-loaded known faces and labels them.
- **Attendance logging:** Records the recognized person's name and time of recognition into a CSV file.
- **CSV file auto-naming:** The CSV filename is dynamically generated based on the date.
- **Face bounding box:** Draws a rectangular box around the detected face and displays the name of the recognized person on the video feed.

## Prerequisites

Before running the project, ensure that you have the following installed on your system:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- Face Recognition (`face-recognition` - depends on `dlib`)

## Installation

1. Clone this repository or download the project files.
2. Install the required dependencies:

    ```bash
    pip install opencv-python numpy face-recognition
    ```

3. Download or prepare the images of the individuals you want the system to recognize. Place them in the project directory and update the file paths in the script.

## Usage

### 1. Prepare Images for Recognition
Ensure the images of the known people are stored locally. Load these images in the script and create encodings for them as follows:

```python
# Example:
deepanshi_image = face_recognition.load_image_file("deep.jpg")
deepanshi_encoding = face_recognition.face_encodings(deepanshi_image)[0]

known_face_encodings = [deepanshi_encoding]
known_face_names = ["Deepanshi"]
```
```python
#Similarly
known_face_encodings = [deepanshi_encoding, sundarP_encoding]
known_face_names = ["Deepanshi", "Sundar Pichai"]
```
2. Run the script:
   ```c
   python smart_face_logger.py
   ```
3. The system will start the webcam feed, detect faces, and log recognized faces into a CSV file named after the date.

   **04-09-2024.csv**
   | Name          | Time              |
   | ------------- | ----------------- |
   | Deepanshi     | 15:32:10          |
   | Sundar Pichai | 15:32:10          |

4. Press `q` to exit the webcam feed and stop the program.

## Customization

- **Adding more known faces:** Add images of new people, encode them using `face_recognition.face_encodings`, and append them to `known_face_encodings` and `known_face_names`.

- **CSV Logging:** The CSV file is named using the format `{date}.csv`. You can modify the logging format or fields in the code.

## Dependencies

- **OpenCV** - For handling video capture and frame processing.
- **NumPy** - For handling numerical operations.
- **Face Recognition** - A powerful library built on top of dlib for face detection and recognition.

## Known Issues

- **Face Detection Accuracy**: If the face detection accuracy is low, try using higher-resolution images or adjusting the scale_factor for resizing the frame.
- **Lighting Conditions**: Poor lighting may affect the performance of face detection. Ensure proper lighting in the room where the system is used.


   




