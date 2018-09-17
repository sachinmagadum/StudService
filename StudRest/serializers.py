from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'age','gender','country','remarks', 'created_at', 'updated_at',)
        model = models.StudentModel

