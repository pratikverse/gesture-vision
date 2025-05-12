# ✋ Hand Gesture Recognition Project

## Overview

This project implements real-time hand gesture recognition using MediaPipe and TensorFlow. It classifies hand keypoints and finger gestures from video input, providing an interactive and user-friendly experience.

## Features

* **Real-time Hand Gesture Recognition:** Recognizes hand gestures from a live video feed.
* **Keypoint Classification:** Classifies hand keypoints using a TensorFlow Lite model.
* **Finger Gesture Classification:** Classifies finger gestures based on point history.
* **Visualization:** Displays hand keypoints, recognized gestures, and other relevant information on the video feed.
* **Interactive Control:** Allows switching between different modes (recognition, keypoint logging, point history logging) and selecting numbers using keyboard input.

## Technical Details

1.  **Hand Landmark Detection**
    * Utilizes MediaPipe Hands to detect hand keypoints from the input video stream.
    * Hand landmarks are extracted as 2D coordinates.

2.  **Keypoint Classification**
    * A TensorFlow Lite model (`keypoint_classifier.tflite`) is used to classify the hand keypoints into specific gestures.
    * The model predicts the gesture category based on the input keypoint data.

3.  **Finger Gesture Classification**
    * A TensorFlow Lite model (`point_history_classifier.tflite`) is used to classify finger movements and gestures based on the history of hand positions.
    * This model analyzes the trajectory of hand movements to recognize dynamic gestures.

4.  **Real-time Processing**
    * The application processes video frames in real-time to provide continuous gesture recognition.
    * FPS (frames per second) is calculated and displayed to monitor performance.

5.  **Application Modes**
    * **Recognition Mode:** Recognizes and displays hand and finger gestures.
    * **Keypoint Logging Mode:** Logs hand keypoint data for model training or analysis.
    * **Point History Logging Mode:** Logs hand position history for finger gesture classification.

## Code Structure

* `app.py`: Python script for the main application, handling video input, hand tracking, gesture recognition, and visualization.
* `keypoint_classifier.py`: Python script containing the `KeyPointClassifier` class, responsible for loading and using the keypoint classification model.
* `point_history_classifier.py`: Python script containing the `PointHistoryClassifier` class, responsible for loading and using the point history classification model.
* `utils/`: Directory containing utility modules.
    * `cvfpscalc.py`: Module for calculating frames per second (FPS).
* `model/`: Directory containing the trained models.
    * `keypoint_classifier/`: Directory containing the keypoint classification model.
        * `keypoint_classifier.tflite`: TensorFlow Lite model for keypoint classification.
        * `keypoint_classifier_label.csv`: Labels for the keypoint classification model.
    * `point_history_classifier/`: Directory containing the point history classification model.
        * `point_history_classifier.tflite`: TensorFlow Lite model for finger gesture classification.
        * `point_history_classifier_label.csv`: Labels for the point history classification model.
* `data/`: Directory containing collected data.
    * `keypoint/`: Directory to store keypoint data.
    * `point_history/`: Directory to store point history data.
* `config.yaml`: Configuration file for application settings.
* `requirements.txt`: List of Python dependencies.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/pratikverse/Hand-Gesture-Recognition.git
    cd Hand Gesture Recognition
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Linux/macOS
    venv\Scripts\activate # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**

    ```bash
    python app.py
    ```

2.  **Interact with the application:**

    * The application will display a live video feed with hand gesture recognition.
    * Press `n` to switch to recognition mode.
    * Press `k` to switch to keypoint logging mode.
    * Press `h` to switch to point history logging mode.
    * Press `0` \~ `9` to select a number.
    * Press `ESC` to exit.

## Dependencies

* Python
* OpenCV (cv2)
* MediaPipe
* TensorFlow
* NumPy

## Data Source

The project uses hand keypoint data and point history data collected from MediaPipe.