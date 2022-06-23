from pickle import TRUE
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto, Categoria
from .serializers import ProductoSerializers,CategoriaSerializers, UserSerializers
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_juegos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializers(producto, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
# Create your views here.


@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_juego(request, codigo):
    try:
        producto = Producto.objects.get(codigo=codigo)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializers(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializers(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_categorias(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializers(categoria, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_categoria(request, codigo):
    try:
        categoria = Categoria.objects.get(codigo=codigo)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategoriaSerializers(categoria)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(categoria, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        serializer = UserSerializers(usuarios, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_usuario(request, id):
    try:
        usuarios = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializers(usuarios)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializers(usuarios, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
