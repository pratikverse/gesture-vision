import numpy as np
import tensorflow as tf


class KeyPointClassifier(object):

    def __init__(
        self,
        model_path='C:/Users/kprat/OneDrive/Desktop/github/gesture-vision/notebooks/model/keypoint_classifier/keypoint_classifier.tflite',  # Default to .tflite
        num_threads=1,
    ):
        print(f"Loading Static classifier model from: {model_path}")  # Debugging
        try:
            self.interpreter = tf.lite.Interpreter(model_path=model_path,
                                                   num_threads=num_threads)
            self.interpreter.allocate_tensors()
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()
        except Exception as e:
            print(f"Error loading TFLite model: {e}")
            raise  # Re-raise the exception to halt execution

    def __call__(
        self,
        landmark_list,
    ):
        input_details_tensor_index = self.input_details[0]['index']
        self.interpreter.set_tensor(
            input_details_tensor_index,
            np.array([landmark_list], dtype=np.float32))
        self.interpreter.invoke()

        output_details_tensor_index = self.output_details[0]['index']

        result = self.interpreter.get_tensor(output_details_tensor_index)

        result_index = np.argmax(np.squeeze(result))

        return result_index