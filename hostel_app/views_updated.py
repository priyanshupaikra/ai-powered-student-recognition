from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
import os
import cv2
import numpy as np
import face_recognition
import pickle
from .models import Student
from .utils import FaceRecognitionUtil, encode_face_for_storage, decode_face_from_storage


def index(request):
    return render(request, 'hostel_app/index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_number = request.POST.get('room_number')
        enrollment_number = request.POST.get('enrollment_number')
        mobile_number = request.POST.get('mobile_number')
        course = request.POST.get('course')
        
        if 'photo' not in request.FILES:
            messages.error(request, 'No photo uploaded')
            return render(request, 'hostel_app/register.html')
        
        photo = request.FILES['photo']
        
        # Save the uploaded file temporarily
        file_name = f"{enrollment_number}_{photo.name}"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        
        # Save file to disk
        path = default_storage.save(file_path, ContentFile(photo.read()))
        
        # Check if student with this enrollment number already exists
        if Student.objects.filter(enrollment_number=enrollment_number).exists():
            messages.error(request, 'Error: Student with this enrollment number already exists')
            if os.path.exists(file_path):
                os.remove(file_path)
            return render(request, 'hostel_app/register.html')
        
        # Encode face
        face_util = FaceRecognitionUtil()
        face_encoding = face_util.encode_face(file_path)
        
        if face_encoding is None:
            messages.error(request, 'No face detected in the image')
            if os.path.exists(file_path):
                os.remove(file_path)
            return render(request, 'hostel_app/register.html')
        
        # Save student to database
        try:
            student = Student(
                name=name,
                room_number=room_number,
                enrollment_number=enrollment_number,
                mobile_number=mobile_number,
                course=course,
                photo_path=file_path
            )
            student.set_face_encoding(face_encoding)
            student.save()
            
            messages.success(request, 'Student registered successfully!')
            return redirect('register')
            
        except IntegrityError as e:
            messages.error(request, 'Error: Student with this enrollment number already exists')
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            messages.error(request, f'Database error: {str(e)}')
            if os.path.exists(file_path):
                os.remove(file_path)
    
    return render(request, 'hostel_app/register.html')


def search(request):
    if request.method == 'POST':
        search_type = request.POST.get('search_type')
        
        if search_type == 'photo':
            if 'search_photo' not in request.FILES:
                messages.error(request, 'No photo uploaded')
                return render(request, 'hostel_app/search.html')
            
            photo = request.FILES['search_photo']
            
            # Save the uploaded file temporarily
            file_name = f"search_{photo.name}"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            
            # Save file to disk
            path = default_storage.save(file_path, ContentFile(photo.read()))
            
            # Encode face
            face_util = FaceRecognitionUtil()
            search_encoding = face_util.encode_face(file_path)
            
            # Remove temporary file
            if os.path.exists(file_path):
                os.remove(file_path)
            
            if search_encoding is None:
                messages.error(request, 'No face detected in the uploaded image')
                return render(request, 'hostel_app/search.html')
            
            # Compare with all students
            students = Student.objects.all()
            best_match = None
            best_distance = float('inf')
            
            for student in students:
                stored_encoding = student.get_face_encoding()
                if stored_encoding is not None:
                    distance = face_recognition.face_distance([stored_encoding], search_encoding)[0]
                    
                    if distance < settings.FACE_RECOGNITION_THRESHOLD and distance < best_distance:
                        best_distance = distance
                        best_match = student
            
            if best_match:
                # Convert file path to URL
                if best_match.photo_path and settings.MEDIA_ROOT in best_match.photo_path:
                    photo_url = best_match.photo_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL.rstrip('/')).replace('\\', '/')
                else:
                    photo_url = best_match.photo_path or ''
                results = [{
                    'id': best_match.id,
                    'name': best_match.name,
                    'room_number': best_match.room_number,
                    'enrollment_number': best_match.enrollment_number,
                    'mobile_number': best_match.mobile_number,
                    'course': best_match.course,
                    'photo_path': photo_url
                }]
                return render(request, 'hostel_app/search.html', {'results': results})
            else:
                messages.error(request, 'No matching student found')
        
        else:
            search_value = request.POST.get('search_value')
            students = Student.objects.all()
            
            if search_type == 'name':
                students = students.filter(name__icontains=search_value)
            elif search_type == 'room_number':
                students = students.filter(room_number=search_value)
            elif search_type == 'enrollment_number':
                students = students.filter(enrollment_number=search_value)
            
            results = []
            for student in students:
                # Convert file path to URL
                if student.photo_path and settings.MEDIA_ROOT in student.photo_path:
                    photo_url = student.photo_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL.rstrip('/')).replace('\\', '/')
                else:
                    photo_url = student.photo_path or ''
                results.append({
                    'id': student.id,
                    'name': student.name,
                    'room_number': student.room_number,
                    'enrollment_number': student.enrollment_number,
                    'mobile_number': student.mobile_number,
                    'course': student.course,
                    'photo_path': photo_url
                })
            
            return render(request, 'hostel_app/search.html', {'results': results})
    
    return render(request, 'hostel_app/search.html')


def admin(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == settings.ADMIN_PASSWORD:
            students = Student.objects.all()
            results = []
            for student in students:
                # Convert file path to URL
                if student.photo_path and settings.MEDIA_ROOT in student.photo_path:
                    photo_url = student.photo_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL.rstrip('/')).replace('\\', '/')
                else:
                    photo_url = student.photo_path or ''
                results.append({
                    'id': student.id,
                    'name': student.name,
                    'room_number': student.room_number,
                    'enrollment_number': student.enrollment_number,
                    'mobile_number': student.mobile_number,
                    'course': student.course,
                    'photo_path': photo_url
                })
            return render(request, 'hostel_app/admin.html', {'students': results, 'authenticated': True})
        else:
            messages.error(request, 'Invalid password')
    
    return render(request, 'hostel_app/admin.html', {'authenticated': False})


def delete_student(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        # Remove photo file
        if os.path.exists(student.photo_path):
            os.remove(student.photo_path)
        student.delete()
        messages.success(request, 'Student deleted successfully')
    except Exception as e:
        messages.error(request, f'Error deleting student: {str(e)}')
    
    return redirect('admin')


def edit_student(request, student_id):
    try:
        student = get_object_or_404(Student, id=student_id)
        
        if request.method == 'POST':
            student.name = request.POST.get('name')
            student.room_number = request.POST.get('room_number')
            student.mobile_number = request.POST.get('mobile_number')
            student.course = request.POST.get('course')
            student.save()
            
            messages.success(request, 'Student updated successfully')
            return redirect('admin')
        
        # Convert file path to URL
        if student.photo_path and settings.MEDIA_ROOT in student.photo_path:
            photo_url = student.photo_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL.rstrip('/')).replace('\\', '/')
        else:
            photo_url = student.photo_path or ''
        student_data = {
            'id': student.id,
            'name': student.name,
            'room_number': student.room_number,
            'enrollment_number': student.enrollment_number,
            'mobile_number': student.mobile_number,
            'course': student.course,
            'photo_path': photo_url
        }
        return render(request, 'hostel_app/edit_student.html', {'student': student_data})
            
    except Exception as e:
        messages.error(request, f'Error updating student: {str(e)}')
        return redirect('admin')


def recognize_face(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Save uploaded image temporarily
            image_file = request.FILES['image']
            file_name = f"temp_frame_{image_file.name}"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            
            # Save file to disk
            path = default_storage.save(file_path, ContentFile(image_file.read()))
            
            # Encode face from the frame
            face_util = FaceRecognitionUtil()
            search_encoding = face_util.encode_face(file_path)
            
            # Remove temporary file
            if os.path.exists(file_path):
                os.remove(file_path)
            
            if search_encoding is None:
                return JsonResponse({'match_found': False, 'error': 'No face detected'})
            
            # Compare with all students
            students = Student.objects.all()
            best_match = None
            best_distance = float('inf')
            
            for student in students:
                stored_encoding = student.get_face_encoding()
                if stored_encoding is not None:
                    distance = face_recognition.face_distance([stored_encoding], search_encoding)[0]
                    
                    if distance < settings.FACE_RECOGNITION_THRESHOLD and distance < best_distance:
                        best_distance = distance
                        best_match = student
            
            if best_match:
                # Convert file path to URL
                if best_match.photo_path and settings.MEDIA_ROOT in best_match.photo_path:
                    photo_url = best_match.photo_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL.rstrip('/')).replace('\\', '/')
                else:
                    photo_url = best_match.photo_path or ''
                
                student_data = {
                    'id': best_match.id,
                    'name': best_match.name,
                    'room_number': best_match.room_number,
                    'enrollment_number': best_match.enrollment_number,
                    'mobile_number': best_match.mobile_number,
                    'course': best_match.course,
                    'photo_path': photo_url
                }
                
                return JsonResponse({'match_found': True, 'student': student_data})
            else:
                return JsonResponse({'match_found': False, 'error': 'No matching student found'})
                
        except Exception as e:
            return JsonResponse({'match_found': False, 'error': str(e)})
    
    return JsonResponse({'match_found': False, 'error': 'Invalid request'})