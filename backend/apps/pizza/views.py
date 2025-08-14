from rest_framework import generics, status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer, PizzaPhotoSerializer


# class PizzaCreateListView(GenericAPIView):
#   # class PizzaCreateListView(APIView):
#     def get(self, request: Request,*args,**kwargs):
# # pizzas = PizzaModel.objects.all()
# #serializer = PizzaSerializer(pizzas, many=True)
# #return Response(serializer.data, status=status.HTTP_200_OK)
#         qs = filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def post(self,*args,**kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class PizzaCreateListView(ListAPIView):
    # queryset = PizzaModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = (AllowAny,)
    # http_method_names = ['post', 'get']
    # def get_queryset(self):
    #     request:Request = self.request
    #     return filter_pizza(request.query_params)

class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):
        request:Request = self.request
        return PizzaFilter(request.query_params)

class PizzaAddPhotoView(UpdateAPIView):
    serializer_class = PizzaPhotoSerializer
    queryset = PizzaModel.objects.all()
    http_method_names = ['put']
    permission_classes = (AllowAny,)
    def perform_update(self, serializer):
        pizza = self.get_object()
        pizza.photo.delete()
        super().perform_update(serializer)



    # http_method_names = ['get', 'delete', 'put', 'patch']

# class PizzaCreateListView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = PizzaSerializer
#     queryset = PizzaModel.objects.all()
#
#     def get_queryset(self):
#         request: Request = self.request
#         return filter_pizza(request.query_params)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

# class PizzaRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = PizzaSerializer
#     queryset = PizzaModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

# class PizzaRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = PizzaModel.objects.all()
# # class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self,*args,**kwargs):
#             # pk = kwargs['pk']
#             # try:
#             #     pizza = PizzaModel.objects.get(pk=pk)
#             # except PizzaModel.DoesNotExist:
#             #     return Response(f'This ID - {pk} is not exist',status=status.HTTP_404_NOT_FOUND)
#         pizza = self.get_object()
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def put(self,*args,**kwargs):
#         pizza = self.get_object()
#         # pk = kwargs['pk']
#         # try:
#         #     pizza = PizzaModel.objects.get(pk=pk)
#         # except PizzaModel.DoesNotExist:
#         #     return Response(f'This ID - {pk} is not exist',status=status.HTTP_404_NOT_FOUND)
#         data = self.request.data
#         serializer = PizzaSerializer(pizza,data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def delete(self,*args,**kwargs):
#         self.get_object().delete()
#         return Response("Deleted !",status=status.HTTP_204_NO_CONTENT)
#         # pk = kwargs['pk']
#         # try:
#         #     PizzaModel.objects.get(pk=pk).delete()
#         # except PizzaModel.DoesNotExist:
#         #     return Response(f'This ID - {pk} does not exist',status=status.HTTP_404_NOT_FOUND)
#         # return Response(f'Id - {pk} is deleted successfully',status=status.HTTP_204_NO_CONTENT)