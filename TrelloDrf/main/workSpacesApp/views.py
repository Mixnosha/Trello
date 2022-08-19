from rest_framework import viewsets, permissions
from workSpacesApp.models import WorkSpaces
from workSpacesApp.serializers import WorkSpaceCreateSerializer, ViewOneWorkspacesSerializer

class WorkspaceModelView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkSpaces.objects.filter(admin_users__user__username=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkSpaceCreateSerializer
        if self.action == 'retrieve':
            return ViewOneWorkspacesSerializer



