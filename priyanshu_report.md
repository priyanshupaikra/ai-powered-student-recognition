
# Minor Project Report
## On
# Hostel Face Recognition System - Django

Submitted in partial fulfilment of the requirements for the award of the degree
of
**BACHELOR OF TECHNOLOGY**
in
**INFORMATION TECHNOLOGY**

**SUBMITTED TO:**
Dr. Udayan Ghosh
Professor

**SUBMITTED BY:**
Priyanshu Paikra
06516401522
7th Semester

## UNIVERSITY SCHOOL OF INFORMATION, COMMUNICATION & TECHNOLOGY
### GGSIPU DWARKA SECTOR 16C, DELHI 110078

---

# INDEX

| S.No. | Title | Page |
|---|---|---|
| 1. | Introduction | 1 |
| 2. | Objectives | 2 |
| 3. | Scope | 3-4 |
| 4. | Requirements Specification | 5-6 |
| 5. | System Design | 7-9 |
| 6. | Technology Stack | 10-11 |
| 7. | Results and Outputs | 12 |
| 8. | Screenshots | 13-15 |
| 9. | Conclusion | 16 |
| 10. | References / Bibliography | 17 |

---

# DECLARATION

I hereby declare that the Minor Project entitled “Hostel Face Recognition System - Django” submitted in partial fulfilment of the requirements for the award of the degree of Bachelor of Technology in Information Technology to the University School of Information, Communication and Technology, Guru Gobind Singh Indraprastha University, Delhi, is a bona fide record of original work carried out by me under the supervision of Dr. Udayan Ghosh, at the same institution.

I further declare that this project report has not been submitted to any other university or institution for the award of any degree or diploma and that the work presented herein is the result of my own research and effort.

**Date:** 05/11/2025
**Place:** Delhi

**Priyanshu Paikra**
06516401522

---

# CERTIFICATE

This is to certify that the Minor Project Report entitled "Hostel Face Recognition System - Django” submitted by Priyanshu Paikra (Enrollment No. 06516401522), student of B.Tech (Information Technology), 7th Semester has been carried out under the guidance of Dr. Udayan Ghosh in partial fulfilment of the requirements for the award of the degree of Bachelor of Technology in Information Technology from the University School of Information, Communication and Technology (USICT), Guru Gobind Singh Indraprastha University, Delhi.

Priyanshu Paikra has demonstrated exceptional commitment, creativity, and technical proficiency throughout the project. His dedication, problem-solving ability, and innovative thinking are highly commendable.

**Dr. Udayan Ghosh**
Professor

---

# ACKNOWLEDGEMENT

The success and final outcome of this project is the result of the invaluable guidance, constant encouragement, and support extended by several individuals, and I feel deeply privileged to have received their assistance throughout the entire project lifecycle. The successful completion of this endeavour stands as a collective achievement, and I wish to express my sincere gratitude to all those who played significant roles in making it possible.

I extend my heartfelt appreciation to the University School of Information, Communication and Technology (USICT), Guru Gobind Singh Indraprastha University, Delhi, for providing me with the opportunity, resources, and academic environment to undertake this project. The support and guidance offered by the institution have been instrumental in navigating the challenges faced during this work.

I express my deepest gratitude to my supervisor, Dr. Udayan Ghosh, Professor, USICT, for his invaluable guidance, motivation, and continuous encouragement throughout the course of this project. His expertise, constructive feedback, and insightful suggestions have greatly contributed to the successful completion of this work.

I also take this opportunity to thank all the faculty members of the Department of Information Technology, whose support, advice, and academic mentorship have shaped my learning experience throughout my studies.

**Priyanshu Paikra**
Enrollment No.: 06516401522
B.Tech (Information Technology)
7th Semester

---

# 1. INTRODUCTION

A comprehensive full-stack web application for hostel student management using advanced face recognition technology powered by deep learning CNN models, now migrated to Django with PostgreSQL. This project aims to provide a secure and efficient way to manage student records in a hostel environment.

---

# 2. ОВЈЕСTIVES

The primary objective of this project is to develop a robust system for hostel student management. The key objectives are:

- **Student Registration**: Register students with personal details and face recognition.
- **Multi-Search Options**: Search by name, room number, enrollment number, or photo.
- **Deep CNN Face Recognition**: Advanced ResNet50-based face recognition with triplet loss.
- **Admin Panel**: Secure admin interface for managing student records.
- **Real-time Processing**: Instant face detection and matching.
- **Responsive Design**: Modern UI with Tailwind CSS.

---

# 3. SCOPE

The scope of this project includes the complete development of a web-based application for hostel management.

## 3.1 Functional Scope:

- **Student Management**: The system allows for the creation, reading, updating, and deletion (CRUD) of student records.
- **Face Recognition**: Students can be identified using their facial features.
- **Search Functionality**: The system provides multiple ways to search for students.
- **Admin Dashboard**: A centralized dashboard for administrators to manage the system.

## 3.2 Technical and Design Scope:

- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Tailwind CSS, JavaScript
- **Machine Learning**: TensorFlow, OpenCV, face_recognition library, Custom CNN

## 3.3 Target Users:

- **Hostel Administration**: To manage student records.
- **Students**: To register and verify their identity.

---

# 4. REQUIREMENTS SPECIFICATION

## 4.1 Functional Requirements:

- **Create/Join Room**: Users must be able to create a new room or join an existing room using a unique Room ID.
- **Real-Time Collaborative Code Editor**: Users should be able to write, edit, and view code in real-time with cursor presence of all participants.
- **Multi-Language Support**: The editor must allow users to select between supported programming languages (JS, TS, C, C++, Java, Python, etc.).
- **Code Execution with Custom Input**: Users should be able to provide input and run their code, and receive output in real-time.
- **Video & Audio Chat**: The system must enable peer-to-peer webcam and microphone streaming among users in a room.
- **Toggle User Media**: Users should be able to toggle their video/audio on or off.

## 4.2 Non-Functional Requirements:

- **Performance**: The system should be able to handle multiple requests with low latency.
- **Scalability**: The system must support a large number of students and administrators.
- **Reliability**: The system must be reliable and available 24/7.
- **Security**: The system must be secure to protect student data.

---

# 5. SYSTEM DESIGN

## 5.1 System Architecture Diagrams:

(You can add system architecture diagrams here)

## 5.2 Module Wise Design:

The application is divided into several modules:

- **Student Registration Module**: Handles the registration of new students.
- **Face Recognition Module**: Handles the face recognition functionality.
- **Search Module**: Handles the search functionality.
- **Admin Module**: Provides an interface for administrators to manage the system.

---

# 6. TECHNOLOGY STACK

- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Tailwind CSS, JavaScript
- **Machine Learning**: TensorFlow, OpenCV, face_recognition library, Custom CNN
- **Image Processing**: OpenCV, PIL

---

# 7. RESULTS AND OUTPUTS

The project successfully implements all the planned features. The system is able to accurately recognize faces and manage student data efficiently. The web interface is user-friendly and responsive.

---

# 8. SCREENSHOTS

(Please add screenshots of your application here. For example: Registration Page, Search Page, Admin Panel, etc.)

---

# 9. CONCLUSION

This project provides a comprehensive solution for hostel management using face recognition. The system is secure, efficient, and easy to use. Future enhancements could include:

- Multi-face detection in single image
- Real-time video recognition
- Mobile application
- Advanced analytics dashboard
- Backup and restore functionality
- Email notifications
- Attendance tracking integration

---

# 10. REFERENCES / BIBLIOGRAPHY

- Django Documentation
- OpenCV Documentation
- TensorFlow Documentation
- face_recognition library documentation
