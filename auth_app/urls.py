from django.urls import path 
from . import views
from .views import register_student
from.views import register_view

urlpatterns = [
# path('',views.register_view,name='register'),
    path('',views.login_view,name='login'),
    path('student_register/', views.register_student, name='student_register'),  # URL for student registration
    path('teacher-register/', views.register_view, name='teacher_register'),
    path('logout/',views.logout_view,name='logout'),
    path('student_dashboard/',views.student_dashboard, name='student_dashboard'),
   # path('teacher_dashboard/',views.dashboard_view,name='teacher-dashboard'),
    #path('display-student-dashboard/',views.student_view ,name='student-dashboard')
]