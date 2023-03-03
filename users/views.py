from rest_framework import generics
from rest_framework.response import Response

from users.models import User, Profile
from users.serializers import UserSerializer, ProfileSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = Profile.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user == instance:
            serializer = self.get_serializer(instance)
        else:
            serializer = ProfileSerializer
        return Response(serializer.data)


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
