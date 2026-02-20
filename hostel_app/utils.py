import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np
import cv2
import os
import face_recognition
import pickle
import base64


class FaceRecognitionUtil:
    def __init__(self):
        pass
    
    def encode_face(self, image_path):
        """Encode face using face_recognition library"""
        try:
            image = face_recognition.load_image_file(image_path)
            # Find all face locations and encodings in the image
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)
            
            if face_encodings:
                # If multiple faces, select the most prominent one (largest bounding box)
                if len(face_encodings) > 1:
                    largest_face_index = self._get_largest_face_index(face_locations)
                    return face_encodings[largest_face_index]
                else:
                    # Return the first (and only) face encoding
                    return face_encodings[0]
            return None
        except Exception as e:
            print(f"Error encoding face: {e}")
            return None
    
    def encode_face_from_array(self, image_array):
        """Encode face from numpy array (for camera frames)"""
        try:
            # Convert BGR to RGB if needed (camera frames are often BGR)
            if len(image_array.shape) == 3 and image_array.shape[2] == 3:
                rgb_image = image_array[:, :, ::-1]  # BGR to RGB
            else:
                rgb_image = image_array
            
            # Find all face locations and encodings in the image
            face_locations = face_recognition.face_locations(rgb_image)
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
            
            if face_encodings:
                # If multiple faces, select the most prominent one (largest bounding box)
                if len(face_encodings) > 1:
                    largest_face_index = self._get_largest_face_index(face_locations)
                    return face_encodings[largest_face_index]
                else:
                    # Return the first (and only) face encoding
                    return face_encodings[0]
            return None
        except Exception as e:
            print(f"Error encoding face from array: {e}")
            return None
    
    def _get_largest_face_index(self, face_locations):
        """Get the index of the face with the largest bounding box"""
        if not face_locations:
            return 0
        
        largest_area = 0
        largest_index = 0
        
        for i, (top, right, bottom, left) in enumerate(face_locations):
            area = (bottom - top) * (right - left)
            if area > largest_area:
                largest_area = area
                largest_index = i
                
        return largest_index
    
    def compare_faces(self, known_encoding, unknown_encoding, threshold=0.6):
        """Compare two face encodings"""
        if known_encoding is None or unknown_encoding is None:
            return False
            
        distance = face_recognition.face_distance([known_encoding], unknown_encoding)[0]
        return distance < threshold, distance
    
    def detect_faces(self, image_path):
        """Detect faces in an image"""
        try:
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)
            return len(face_locations) > 0
        except Exception as e:
            print(f"Error detecting faces: {e}")
            return False


class DeepFaceRecognitionModel:
    def __init__(self, input_shape=(224, 224, 3)):
        self.input_shape = input_shape
        self.model = self.create_model()
    
    def create_model(self):
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            BatchNormalization(),
            MaxPooling2D(2, 2),
            
            Conv2D(64, (3, 3), activation='relu'),
            BatchNormalization(),
            MaxPooling2D(2, 2),
            
            Conv2D(128, (3, 3), activation='relu'),
            BatchNormalization(),
            MaxPooling2D(2, 2),
            
            Conv2D(256, (3, 3), activation='relu'),
            BatchNormalization(),
            MaxPooling2D(2, 2),
            
            Conv2D(512, (3, 3), activation='relu'),
            BatchNormalization(),
            MaxPooling2D(2, 2),
            
            Flatten(),
            Dense(1024, activation='relu'),
            Dropout(0.5),
            Dense(512, activation='relu'),
            Dropout(0.5),
            Dense(256, activation='relu'),
            Dropout(0.3),
            Dense(128, activation='linear')
        ])
        
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='mean_squared_error',
            metrics=['accuracy']
        )
        
        return model
    
    def preprocess_image(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        image = image.astype('float32') / 255.0
        return np.expand_dims(image, axis=0)
    
    def extract_features(self, image_path):
        processed_image = self.preprocess_image(image_path)
        features = self.model.predict(processed_image)
        return features[0]
    
    def save_model(self, filepath):
        self.model.save(filepath)
    
    def load_model(self, filepath):
        self.model = tf.keras.models.load_model(filepath)


def encode_face_for_storage(encoding):
    """Convert numpy array to base64 string for storage"""
    if encoding is not None:
        return base64.b64encode(pickle.dumps(encoding)).decode('utf-8')
    return None


def decode_face_from_storage(encoded_string):
    """Convert base64 string back to numpy array"""
    if encoded_string:
        try:
            decoded = base64.b64decode(encoded_string.encode('utf-8'))
            return pickle.loads(decoded)
        except:
            return None
    return None