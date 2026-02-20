import os
import django
from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
import certifi
from hostel_app.models import Student
import datetime


class Command(BaseCommand):
    help = 'Migrate data from MongoDB to PostgreSQL'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mongo-uri',
            type=str,
            help='MongoDB URI',
            default=getattr(settings, 'MONGO_URI', '')
        )
        parser.add_argument(
            '--mongo-db-name',
            type=str,
            help='MongoDB database name',
            default=getattr(settings, 'MONGO_DB_NAME', 'hostel_db')
        )

    def handle(self, *args, **options):
        self.stdout.write('Starting data migration from MongoDB to PostgreSQL...')
        
        # Connect to MongoDB
        try:
            client = MongoClient(
                options['mongo_uri'],
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=5000,
                tls=True,
                retryWrites=True,
                w='majority'
            )
            client.admin.command('ping')
            self.stdout.write(self.style.SUCCESS('Successfully connected to MongoDB'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to connect to MongoDB: {e}'))
            return

        # Get MongoDB collection
        db = client[options['mongo_db_name']]
        collection = db.students

        # Migrate data
        migrated_count = 0
        for doc in collection.find():
            try:
                student = Student(
                    name=doc.get('name', ''),
                    room_number=doc.get('room_number'),
                    enrollment_number=doc.get('enrollment_number', ''),
                    mobile_number=doc.get('mobile_number'),
                    course=doc.get('course'),
                    photo_path=doc.get('photo_path'),
                    face_encoding=doc.get('face_encoding'),
                    created_at=doc.get('created_at', datetime.datetime.now())
                )
                student.save()
                migrated_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error migrating student {doc.get("enrollment_number", "unknown")}: {e}'))

        self.stdout.write(
            self.style.SUCCESS(f'Successfully migrated {migrated_count} students from MongoDB to PostgreSQL')
        )