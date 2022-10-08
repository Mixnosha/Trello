from rest_framework import viewsets, permissions
from status.models import StatusWK, StatusBoards
from status.serializers import StatusViewSerializer


class StatusAllView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.kwargs['some'] == 'wk':
            return StatusWK.objects.all()
        elif self.kwargs['some'] == 'br':
            return StatusBoards.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return StatusViewSerializer
