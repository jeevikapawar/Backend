from django.shortcuts import redirect
from .models import Student, Teacher

# ******* Authenticated *******
def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped_view

# ******* Guest *******
def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        print("request user:", request.user)
        if request.user.is_authenticated:
            if Student.objects.filter(user=request.user).exists():
                return redirect('student_dashboard')
            # Check if the user is a teacher
            elif Teacher.objects.filter(user=request.user).exists():
                return redirect('teacher_dashboard')
        return view_function(request, *args, **kwargs)
    return wrapped_view

