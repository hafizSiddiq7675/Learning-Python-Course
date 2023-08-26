from django.urls import path
from .views import GetStudentsView

urlpatterns = [
    path('students/', GetStudentsView.as_view(), name='get-students'),
]
