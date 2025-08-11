from distutils.dep_util import newer
from urllib import request

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms import model_to_dict

from fruits.models import NewFruitModel


class FruitsView(APIView):
    def get(self,*args,**kwargs):
        all_fruits = NewFruitModel.objects.all()
        response = [model_to_dict(i) for i in all_fruits]
        return Response(response)


    def post(self,*args,**kwargs):
        data = self.request.data
        fruit_ex = NewFruitModel.objects.create(**data)
        fruit_ex.save()
        return Response(model_to_dict(fruit_ex))
    def put(self,*args,**kwargs):
        pk = **kwargs['pk']
        pass
    def delete(self,*args,**kwargs):
        pass


