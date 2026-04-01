from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import StudentSerializers
from .models import Student
from .permission import IsAdmin_or_SuperAdmin

class StudentViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated,IsAdmin_or_SuperAdmin]
    authentication_classes = [JWTAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers