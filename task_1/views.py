from rest_framework import generics
from rest_framework.permissions import AllowAny

from task_1.models import User
from task_1.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
