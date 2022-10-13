from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from boardsApp.models import Boards
from boardsApp.serializers import ViewOneBoardSerializer
from columnApp.models import Column
from columnApp.serializers import ColumnAllViewSerializer, ColumnOneViewSerializer


class ColumnModelCRUD(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    def get_queryset(self):
        return Column.objects.all()

    serializer_class = ColumnOneViewSerializer


@api_view(['GET'])
def ColumnList(request, pk):
    """
    get column list pk == id board
    """
    if request.method == 'GET':
        clm_pk = Boards.objects.filter(id=pk).values_list('column', flat=True)
        data = ColumnAllViewSerializer(Column.objects.filter(id__in=list(clm_pk)), many=True)
        return Response(data.data)
