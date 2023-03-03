from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from school.models import Course, Lesson
from school.serializers import CourseSerializer, LessonSerializer
from school.permissions import UserChangeLessonPermissionManager, UserChangeCoursePermissionManager, \
    UserRetrieveCoursePermissionManager, UserRetrieveLessonPermissionManager


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'update': [UserChangeCoursePermissionManager],
        'partial_update': [UserChangeCoursePermissionManager],
        'list': [IsAdminUser],
        'retrieve': [UserRetrieveCoursePermissionManager],
        'destroy': [IsAdminUser]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [UserRetrieveLessonPermissionManager]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'slug'


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [UserChangeLessonPermissionManager]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'slug'
