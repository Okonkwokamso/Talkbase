from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def welcome(request):
  return Response({
    "message": "Welcome to Talkbase!",
    "status": "success",
    "documentation": "Visit /docs for API documentation."
  })






