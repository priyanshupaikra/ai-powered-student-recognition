from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('admin/', views.admin, name='admin'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('recognize_face/', views.recognize_face, name='recognize_face'),
]