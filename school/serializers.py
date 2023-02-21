from rest_framework import serializers
from school.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'name',
            'course',
            'preview',
            'description',
            'slug'
        )


class CourseSerializer(serializers.ModelSerializer):
    lesson_num = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = (
            'name',
            'preview',
            'description',
            'lesson_num',
            'lessons'
        )

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons')
        course = Course.objects.create(**validated_data)
        for lesson_data in lessons_data:
            Lesson.objects.create(course=course, **lesson_data)
        return course

    def get_lesson_num(self, instance):
        lessons = Lesson.objects.filter(course=instance).all().count()
        if lessons:
            return lessons
        return 0
