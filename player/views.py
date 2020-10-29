from django import views
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from player.models import Author
from player.serializers import AuthorSerializer, AuthorSerialzierGet
from rest_framework.views import APIView

class AuthorApiView(APIView):

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        #instance = Author.objects.create(**request.data)
        return Response(AuthorSerializer(instance).data)

    def get(self, request):
        return Response(AuthorSerializer(Author.objects.all(), many=True).data)