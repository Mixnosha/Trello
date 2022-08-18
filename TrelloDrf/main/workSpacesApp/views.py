from rest_framework import viewsets, permissions
from rest_framework.response import Response

from workSpacesApp.models import WorkSpaces
from workSpacesApp.serializers import ViewAllWorkspacesSerializer


class WorkSpacesView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = WorkSpaces.objects.filter(user__user__username=request.user)
        serializer = ViewAllWorkspacesSerializer(queryset)
        return Response(serializer.data)

