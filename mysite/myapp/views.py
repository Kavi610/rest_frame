# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import User
from serializers import UserSerializer
# Create your views here.
@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

#get single user
@api_view(['GET'])
def getUser(request,pk):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return Response(serializer.data)
    
#add user
@api_view(['GET'])
def addUser(request):
    user=User.objects.all()
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update user
@api_view(['PUT'])
def updateUser(request,pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete user
#add user
@api_view(['DELETE'])
def deleteUser(request,pk):
    user=User.objects.get(id=pk)
    serializer=UserSerializer(data=request.data)
    user.delete()
    return Response("item successfully deleted")