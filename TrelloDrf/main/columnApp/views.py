from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from boardsApp.models import Boards
from boardsApp.serializers import ViewOneBoardSerializer
from columnApp.models import Column
from columnApp.serializers import ColumnAllViewSerializer


class ColumnModelCLUD(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    def get_queryset(self):
        return Column.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ColumnAllViewSerializer


class ColumnModelRetrieve(
    mixins.RetrieveModelMixin,
    GenericViewSet):

    def get_object(self):
        pk = Boards.objects.filter(id=self.kwargs['pk']).values_list('column', flat=True)
        ag = Column.objects.filter(id__in=list(pk))
        print(ag)
        return ag[0]
    serializer_class = ColumnAllViewSerializer
