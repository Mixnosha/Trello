from django.shortcuts import render
from rest_framework import viewsets, permissions

from commentApp.models import Status
from commentApp.serializers import StatusViewSerializer


class StatusAllView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Status.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return StatusViewSerializer
