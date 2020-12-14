import json

from django import views
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from player.models import Author, Statistic
from player.serializers import AuthorSerializer, AuthorSerialzierGet, StatisticSerializer, StatisticSerializerGet
from rest_framework.views import APIView

class AuthorApiView(APIView):

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        #instance = Author.objects.create(**request.data)
        return Response(AuthorSerializer(instance).data)

    def get(self, request):
        print(request.data)
        print(request.GET)
        print('HERE')
        return Response({"response": 200, "data": 111})


class StatisticView(APIView):

    def post(self, request):

        serializer = StatisticSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        # instance = Author.objects.create(**request.data)
        return Response(StatisticSerializer(instance).data)

    def put(self, request):
        serializer_get = StatisticSerializerGet(data=request.GET)
        serializer_get.is_valid(raise_exception=True)
        statistic_instance = Statistic.objects.get(id=request.GET.get('id'))
        serializer_update = StatisticSerializer(instance=statistic_instance,
                                                data=request.data)
        serializer_update.is_valid(raise_exception=True)
        instance = serializer_update.save()
        return Response(data=StatisticSerializer(instance).data)

    def get(self, request):

        return Response(StatisticSerializer(Statistic.objects.last()).data)