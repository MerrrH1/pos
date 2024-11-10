from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from pos_app.models import (
    User, Category, OrderMenuDetail, MenuResto, StatusModel, OrderMenu, Profile, TableResto
)
from api.serializers import (
    UserSerializer, CategorySerializer, OrderMenuDetailSerializer, MenuRestoSerializer, StatusModelSerializer,
    OrderMenuSerializer, ProfileSerializer, TableRestoSerializer
)

class CategoryListApiView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name' : request.data.get('name'),
        }
        serializer = CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Data Created Successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id = id)
        except Category.DoesNotExist:
            return None
        
    def get(self, request, id, *args, **kwargs):
        category_instances = self.get_object(id)
        if not category_instances:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data does not exists...',
                    'data' : {}
                }, status = status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(category_instances)
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data Retrieved Successfully',
            'data' : serializer.data
        }
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, id, *args, **kwargs):
        category_instance = self.get_object(id)
        if not category_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data does not exists...',
                    'data' : {}
                }, status = status.HTTP_404_NOT_FOUND
            )
        data = {
            'name' : request.data.get('name'),
        }
        serializer = CategorySerializer(instance = category_instance, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Data Created Successfully...',
                'data' : serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, *args, **kwargs):
        category_instance = self.get_object(id)
        if not category_instance:
            return Response(
                {
                    'status' : status.HTTP_404_NOT_FOUND,
                    'message' : 'Data does not exists...',
                    'data' : {}
                }, status = status.HTTP_404_NOT_FOUND
            )
        category_instance.delete()
        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Data Deleted Successfully...'
        }
        return Response(response, status = status.HTTP_200_OK)