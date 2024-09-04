import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load known images
deepanshi_image = face_recognition.load_image_file("deep.jpg")
deepanshi_encoding = face_recognition.face_encodings(deepanshi_image)[0]
name2_image = face_recognition.load_image_file("deep2.jpg")
name2_encoding = face_recognition.face_encodings(name2_image)[0]
known_face_encodings = [deepanshi_encoding, name2_encoding]
known_face_names = ["deepanshi", "name2"]

# Initialize CSV filename
csv_filename = None

while True:
    _, frame = video_capture.read()

    # Increase the frame size by resizing
    scale_factor = 1.5  # Increase the size of the frame
    frame = cv2.resize(frame, (0, 0), fx=scale_factor, fy=scale_factor)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            current_date = datetime.now().strftime("%d-%m-%Y")
            time = datetime.now().strftime("%H:%M:%S")

            # Create or update CSV file with the recognized name in the filename
            if not csv_filename:
                csv_filename = f"{name}_{current_date}.csv"
                f = open(csv_filename, "w+", newline='')
                csv_writer = csv.writer(f)
                csv_writer.writerow(["Name", "Time"])  # Add header to CSV

            # Write attendance to CSV
            csv_writer.writerow([name, time])

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow("attendance", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
f.close()
video_capture.release()
cv2.destroyAllWindows()
