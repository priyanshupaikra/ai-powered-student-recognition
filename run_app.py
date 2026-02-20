#!/usr/bin/env python
"""
Run script for the Hostel Face Recognition Django Application
"""
import os
import sys
import subprocess

def check_mongodb():
    """Check if MongoDB is running"""
    try:
        # Try to connect to MongoDB
        import pymongo
        client = pymongo.MongoClient('localhost', 27017, serverSelectionTimeoutMS=2000)
        client.server_info()  # Will raise an exception if can't connect
        print("✓ MongoDB is running")
        return True
    except Exception as e:
        print(f"✗ MongoDB is not running: {e}")
        return False

def main():
    print("=== Hostel Face Recognition System ===")
    
    # Check if MongoDB is running
    if not check_mongodb():
        print("\nPlease start MongoDB before running the application:")
        print("  Windows: net start MongoDB")
        print("  Linux/macOS: sudo systemctl start mongod")
        sys.exit(1)
    
    print("\nStarting Django development server...")
    print("Access the application at: http://127.0.0.1:8000/")
    print("Admin panel at: http://127.0.0.1:8000/admin/")
    print("Press CTRL+C to stop the server\n")
    
    try:
        # Run the Django development server
        subprocess.run([sys.executable, 'manage.py', 'runserver'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Django server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()