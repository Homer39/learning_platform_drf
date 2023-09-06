from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from materials.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
