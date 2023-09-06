from rest_framework import serializers

from materials.models import Course
from materials.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, source='lesson', read_only=True)
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson.count()
