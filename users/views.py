from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from materials.services.permissions import IsStaff, IsOwner
from users.models import User
from users.serializers import UserListSerializer, UserDe, UserDetailSerializer


class UserViewSet(ModelViewSet):
    """Вью сет для пользователя"""
    queryset = User.objects.all()
    serializer = UserListSerializer

    def get_permissions(self):
        """Права доступа"""
        if self.action == 'retrive':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'create':
            permission_classes = [IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        """При выводе пользователя будет видна история платежей"""
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
