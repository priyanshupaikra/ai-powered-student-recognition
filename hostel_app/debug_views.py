from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
import face_recognition
import numpy as np


def debug_face_encodings(request):
    """Debug function to check face encodings in the database"""
    if request.method == 'GET':
        try:
            students = Student.objects.all()
            encoding_info = []
            
            for student in students:
                encoding = student.get_face_encoding()
                if encoding is not None:
                    # Check if encoding is valid
                    try:
                        # Try to use the encoding
                        if isinstance(encoding, np.ndarray):
                            encoding_info.append({
                                'student_name': student.name,
                                'student_id': student.id,
                                'encoding_type': str(type(encoding)),
                                'encoding_shape': encoding.shape if hasattr(encoding, 'shape') else 'No shape',
                                'is_valid': True
                            })
                        else:
                            encoding_info.append({
                                'student_name': student.name,
                                'student_id': student.id,
                                'encoding_type': str(type(encoding)),
                                'encoding_shape': 'N/A',
                                'is_valid': False,
                                'error': 'Encoding is not a numpy array'
                            })
                    except Exception as e:
                        encoding_info.append({
                            'student_name': student.name,
                            'student_id': student.id,
                            'encoding_type': str(type(encoding)),
                            'is_valid': False,
                            'error': str(e)
                        })
                else:
                    encoding_info.append({
                        'student_name': student.name,
                        'student_id': student.id,
                        'encoding_type': 'None',
                        'is_valid': False,
                        'error': 'No encoding found'
                    })
            
            return JsonResponse({
                'total_students': len(students),
                'encoding_info': encoding_info
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    return JsonResponse({'error': 'Invalid request method'})