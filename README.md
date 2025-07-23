# GESTURE VISION

## OVERVIEW

This project implements real-time hand gesture recognition using MediaPipe and TensorFlow. It classifies hand keypoints and finger gestures from video input, providing an interactive and user-friendly experience.

## FEATURES

* **REAL TIME GESTURE RECOGNITION:** Recognizes hand gestures from a live video feed.
* **KEYPOINT CLASSIFICATION:** Classifies hand keypoints using a TensorFlow Lite model.
* **FINGER GESTURE CLASSIFICATION:** Classifies finger gestures based on point history.
* **VISUALISATION:** Displays hand keypoints, recognized gestures, and other relevant information on the video feed.
* **INTERACTIVE CONTROL:** Allows switching between different modes (recognition, keypoint logging, point history logging) and selecting numbers using keyboard input.

## TECHNICAL DETAILS

1.  **HAND LANDMARK DETECTION**
    * Utilizes MediaPipe Hands to detect hand keypoints from the input video stream.
    * Hand landmarks are extracted as 2D coordinates.

2.  **KEYPOINT CLASSIFICATION**
    * A TensorFlow Lite model (`keypoint_classifier.tflite`) is used to classify the hand keypoints into specific gestures.
    * The model predicts the gesture category based on the input keypoint data.

3.  **FINGER GESTURE CLASSIFICATION**
    * A TensorFlow Lite model (`point_history_classifier.tflite`) is used to classify finger movements and gestures based on the history of hand positions.
    * This model analyzes the trajectory of hand movements to recognize dynamic gestures.

4.  **REAL TIME PROCESSING**
    * The application processes video frames in real-time to provide continuous gesture recognition.
    * FPS (frames per second) is calculated and displayed to monitor performance.

5.  **APPLICATION MODES**
    * **Recognition Mode:** Recognizes and displays hand and finger gestures.
    * **Keypoint Logging Mode:** Logs hand keypoint data for model training or analysis.
    * **Point History Logging Mode:** Logs hand position history for finger gesture classification.

## DATA SOURCE

The project uses hand keypoint data and point history data collected from MediaPipe.

## INTERACTION WITH THE INTERFACE

* The application will display a live video feed with hand gesture recognition.
    * Press `n` to switch to recognition mode.
    * Press `k` to switch to keypoint logging mode.
    * Press `h` to switch to point history logging mode.
    * Press `0` \~ `9` to select a number.
    * Press `ESC` to exit.
