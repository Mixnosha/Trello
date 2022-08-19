from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from workSpacesApp.models import WorkSpaces
from workSpacesApp.serializers import WorkSpaceCreateSerializer, ViewOneWorkspacesSerializer

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Получение всех рабочих пространств залогиненого пользователя"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Создание рабочего пространства"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Получение одного рабочего пространства залогиненного пользователя"
))
class WorkspaceModelView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkSpaces.objects.filter(admin_users__user__username=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkSpaceCreateSerializer
        if self.action == 'retrieve':
            return ViewOneWorkspacesSerializer



