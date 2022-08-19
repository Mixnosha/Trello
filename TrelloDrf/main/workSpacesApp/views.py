from rest_framework import viewsets, permissions
from rest_framework.response import Response
from workSpacesApp.models import WorkSpaces
from workSpacesApp.serializers import ViewAllWorkspacesSerializer, ViewWorkspacesSerializer, WorkSpaceCreateSerializer


class WorkSpacesView(viewsets.ViewSet):
    """API рабочее пространство """
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = WorkSpaces.objects.filter(admin_users__user__username=request.user)
        try:
            serializer = ViewAllWorkspacesSerializer(queryset, many=True)
        except Exception:
            return Response({'status': 'no workspaces'})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            queryset = WorkSpaces.objects.get(id=pk)
            print(queryset.boards)
        except Exception as e:
            return Response({'error': str(e)})
        try:
            serializer = ViewWorkspacesSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status': str(e)})

class WorkspaceModelView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkSpaces.objects.filter(admin_users__user__username=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkSpaceCreateSerializer
        else:
            return ViewWorkspacesSerializer



