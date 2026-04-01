from rest_framework import serializers

from .models import CustomUser,Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['telegram_id']