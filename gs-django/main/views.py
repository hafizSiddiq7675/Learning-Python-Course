from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination


class GetStudentsView(APIView):

    def get(self, request):
        students = Student.objects.all()
        paginator = PageNumberPagination()
        paginated_students = paginator.paginate_queryset(students, request)
        
        serializer = StudentSerializer(paginated_students, many=True)
        return paginator.get_paginated_response(serializer.data)
