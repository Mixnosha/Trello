from rest_framework import viewsets, permissions
from rest_framework.response import Response
from workSpacesApp.models import WorkSpaces
from workSpacesApp.serializers import ViewAllWorkspacesSerializer, ViewWorkspacesSerializer


class WorkSpacesView(viewsets.ViewSet):
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
        except Exception as e:
            return Response({'error': str(e)})
        try:
            serializer = ViewWorkspacesSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status': str(e)})
#Дописать сериалайзер на Boards