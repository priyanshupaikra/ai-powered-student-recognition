#!/usr/bin/env python
import os
import sys
# import django
from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks and start the Django development server."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostel_face_recognition.settings')
    
    # Check if we're running the server command
    if 'runserver' in sys.argv:
        print("=== Hostel Face Recognition System ===")
        print("Starting Django development server...")
        print("Access the application at: http://127.0.0.1:8000/")
        print("Admin panel available at: http://127.0.0.1:8000/admin/")
        print("Press CTRL+C to stop the server")
        print()
    
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error running command: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
