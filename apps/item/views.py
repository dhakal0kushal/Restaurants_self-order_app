# Django imports
from django.shortcuts import render
from django.http import JsonResponse
# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Serializer Class imports
from .serializers import CategorySerializer, ItemSerializer
# Model Class imports
from .models import Category, Item


# APIs for category and Item
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Category List':'/category-list',
    'Category Detail View':'/category-detail/<str:pk>',
    'Category Create':'/category-create',
    'Category Update':'/category-update/<str:pk>',
    'Category Delete':'/category-delete/<str:pk>',

    'ItemList':'/item-list',
    'Item Detail View':'/item-detail/<str:pk>',
    'Item Create':'/item-create',
    'Item Update':'/item-update/<str:pk>',
    'Item Delete':'/item-delete/<str:pk>',
    }
  return Response(api_urls)

# methods for category 

@api_view(['GET'])
def categoryList(request):
  categories = Category.objects.all().order_by('-id')
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(category, many=False)
  return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
  serializer = CategorySerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['POST'])
def categoryUpdate(request, pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(instance=category, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['DELETE'])
def categoryDelete(request, pk):
  category = Category.objects.get(id=pk)
  category.delete()
  return Response('Category succsesfully delete!')

# methods for Items
@api_view(['GET'])
def itemList(request):
  try:
    items = Item.objects.all().order_by('-id')
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
    serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = ItemSerializer(item, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
  if request.method == "POST":
    serializer = ItemSerializer(data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save()
      data["success"]="Create Successful"
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def itemUpdate(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == "POST":
    serializer = ItemSerializer(instance=item, data=request.data)
    data={}
    if serializer.is_valid():
      serializer.save()
      data["success"]="update Successful"
      return Response (data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def itemDelete(request, pk):
  try:
    item = Item.objects.get(id=pk)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "DELETE":
    operation = item.delete()
    data={}
    if operation:
      data["success"]="Delete Successful"
    else:
      data["failure"]="Delete Failed"
    return Response(data=data)

