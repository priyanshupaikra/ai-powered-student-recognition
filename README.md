# Hostel Face Recognition System - Django

A comprehensive full-stack web application for hostel student management using advanced face recognition technology powered by deep learning CNN models, now migrated to Django with PostgreSQL.

## Features

- **Student Registration**: Register students with personal details and face recognition
- **Multi-Search Options**: Search by name, room number, enrollment number, or photo
- **Deep CNN Face Recognition**: Advanced ResNet50-based face recognition with triplet loss
- **Admin Panel**: Secure admin interface for managing student records
- **Real-time Processing**: Instant face detection and matching
- **Responsive Design**: Modern UI with Tailwind CSS

## Technology Stack

- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Tailwind CSS, JavaScript
- **Machine Learning**: TensorFlow, OpenCV, face_recognition library, Custom CNN
- **Image Processing**: OpenCV, PIL

## File Structure

```
hostel-face-recognition-django/
├── manage.py                 # Django management script
├── run.py                    # Application runner
├── install_django.py         # Installation script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── hostel_face_recognition/  # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── hostel_app/              # Main application
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL configuration
│   ├── utils.py             # Utility functions
│   └── migrations/          # Database migrations
├── static/                  # Static files
│   ├── uploads/             # Uploaded images storage
│   ├── css/                 # CSS files
│   └── js/                  # JavaScript files
└── templates/               # HTML templates
    └── hostel_app/          # App-specific templates
```

## Installation

### Prerequisites

- Python 3.8+
- MongoDB Community Server
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hostel-face-recognition-django
   ```

2. **Run installation script**
   ```bash
   python install_django.py
   ```

3. **Setup PostgreSQL Database**
   - Install PostgreSQL
   - Create a database named `hostel_db`
   - Update the `.env` file with your database credentials:
     ```
     DB_NAME=hostel_db
     DB_USER=postgres
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Migrate data from MongoDB (if applicable)**
   ```bash
   python manage.py migrate_from_mongo
   ```

6. **Run the application**
   ```bash
   python run.py runserver
   ```

7. **Access the application**
   - Open browser and navigate to: `http://127.0.0.1:8000`

## Usage

### Student Registration

1. Navigate to the registration page
2. Fill in student details:
   - Full Name
   - Room Number
   - Enrollment Number (unique)
   - Mobile Number
   - Course (B.Tech, M.Tech, BCA, MCA, B.Sc, M.Sc, MBA, PhD)
   - Upload a clear face photo
3. Submit the form

### Student Search

1. Go to the search page
2. Choose search method:
   - **By Name**: Enter student name
   - **By Room Number**: Enter room number
   - **By Enrollment Number**: Enter enrollment number
   - **By Photo**: Upload a photo for face recognition
3. View search results

### Admin Panel

1. Access admin panel from home page
2. Enter admin password: `admin123`
3. View all registered students
4. Edit or delete student records

## Deep Learning Model

The system uses an advanced CNN architecture:

- **Base Model**: ResNet50 pre-trained on ImageNet
- **Custom Layers**: Dense layers with batch normalization and dropout
- **Loss Function**: Triplet loss for face embedding learning
- **Features**: 512-dimensional face embeddings
- **Similarity Metric**: Cosine similarity and Euclidean distance

## Database Schema

### Students Table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    room_number VARCHAR(20),
    enrollment_number VARCHAR(50) UNIQUE,
    mobile_number VARCHAR(15),
    course VARCHAR(100),
    photo_path VARCHAR(255),
    face_encoding TEXT,
    created_at TIMESTAMP
);
```

## Configuration

The application uses Django settings for configuration in `hostel_face_recognition/settings.py`:

- Database connection settings
- File upload settings
- Face recognition thresholds
- Admin password

## Security Features

- Secure file upload with type validation
- MongoDB injection protection
- Admin authentication
- Unique constraint on enrollment numbers
- Input sanitization

## Performance Optimization

- Efficient face encoding storage using base64 encoding
- Optimized CNN inference
- Batch processing capabilities
- Image preprocessing pipeline
- Database indexing on frequently queried fields

## Troubleshooting

### Common Issues

1. **PostgreSQL Connection Error**
   - Ensure PostgreSQL server is running
   - Verify database credentials in `.env` file
   - Check if PostgreSQL is accepting connections on port 5432

2. **Face Detection Failed**
   - Ensure uploaded image has a clear, visible face
   - Check image format (JPG, PNG supported)
   - Verify proper lighting in the photo

3. **Package Installation Error**
   - Install CMAKE: `pip install cmake`
   - Install dlib: `pip install dlib`
   - For Windows: Install Visual Studio Build Tools
   - For PostgreSQL support: `pip install psycopg2-binary`

4. **Model Loading Error**
   - Check if TensorFlow is properly installed
   - Verify model file path
   - Ensure sufficient system memory

5. **Migration Issues**
   - Ensure all dependencies are installed
   - Check that the database is accessible
   - Verify that the migration files are correct

## API Endpoints

- `GET /` - Home page
- `GET,POST /register/` - Student registration
- `GET,POST /search/` - Student search
- `GET,POST /admin/` - Admin panel
- `GET /delete_student/<id>/` - Delete student
- `GET,POST /edit_student/<id>/` - Edit student

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Add tests
5. Submit pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Create an issue on GitHub
- Contact the development team
- Check documentation and troubleshooting guide

## Future Enhancements

- Multi-face detection in single image
- Real-time video recognition
- Mobile application
- Advanced analytics dashboard
- Backup and restore functionality
- Email notifications
- Attendance tracking integration