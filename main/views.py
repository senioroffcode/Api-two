import rest_framework.status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import action


# class ClientView(ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
#     def calculate(self, query):
#         return query.count()
#
#     def list(self, request):
#         client = self.queryset
#         ser = self.serializer_class(client, many=True).data
#         data = {
#             'count': self.calculate(client),
#             "clients": ser,
#         }
#         return Response(data)
#
#     def create(self, request):   #POST
#         pass
#
#     def retrieve(self, request, pk=None):     #GET single object
#         pass
#
#     def update(self, request, pk=None):             # PUT
#         pass
#
#     # def partial_update(self, request, pk=None):             # PATCH
#     #     pass
#
#     def destroy(self, request, pk=None):                #delete
#         return Response('asckaskc', status=rest_framework.status.HTTP_204_NO_CONTENT)

# class ClientView(ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     http_method_names = ['get', 'post']


class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        count = self.queryset.count()
        min = 55
        max = 44
        data = {
            "count": count,
            "min": min,
            "max": max
        }
        return Response(data)


# class ClientView(ReadOnlyModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
