
from rest_framework import serializers
from projects.models import Project,Tag


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'