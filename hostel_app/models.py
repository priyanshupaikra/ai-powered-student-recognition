from django.db import models
import datetime
import base64
import pickle


class Student(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20, blank=True, null=True)
    enrollment_number = models.CharField(max_length=50, unique=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True)
    face_encoding = models.TextField(blank=True, null=True)  # Store base64 encoded pickle data
    created_at = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.name

    def set_face_encoding(self, encoding):
        """Convert numpy array to base64 string for storage"""
        if encoding is not None:
            encoded = base64.b64encode(pickle.dumps(encoding)).decode('utf-8')
            self.face_encoding = encoded

    def get_face_encoding(self):
        """Convert base64 string back to numpy array"""
        if self.face_encoding:
            try:
                decoded = base64.b64decode(self.face_encoding.encode('utf-8'))
                return pickle.loads(decoded)
            except:
                return None
        return None

    class Meta:
        db_table = 'students'