from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin

from .models import ApiData
from .serializers import Dataserializer

# Create your views here.

class ApiDataListView(APIView,UpdateModelMixin,DestroyModelMixin):
    serializer_class=Dataserializer

    def get(self,request,id=None):
        if id:
            try:
                queryset=ApiData.objects.get(id=id)
            except ApiData.DoesNotExist:
                
                #if doesn't exist return error response
                return Response({'error':'This todo item does not exist.'},status=400)
            read_serializer=Dataserializer(queryset)
        else:
            # get all data from model
            queryset=ApiData.objects.all() 
            
            # conversion of django queryset object to JSON format 
            read_serializer=Dataserializer(queryset,many=True)   
            
        return Response(read_serializer.data) 
    
    def post(self,request):
        craete_serializer=Dataserializer(data=request.data)
        
        if craete_serializer.is_valid():
            correct=craete_serializer.save()
            
            read_serializer=Dataserializer(correct)
            
            return Response(read_serializer.data,status=201)
        
        return Response(craete_serializer.errors,status=400)
    
    def put(self,request,id=None):
        try:
            api_data=ApiData.objects.get(id=id)
        except ApiData.DoesNotExist:
            return Response({'error : ':'This todo item does not exist.'},status=400)
        
        update_serializer=Dataserializer(api_data,data=request.data)
        
        if update_serializer.is_valid():
            correct=update_serializer.save()
            read_serializer=Dataserializer(correct)
            return Response(read_serializer.data,status=200)
        
        return Response(update_serializer.errors,status=400)
    
    def delete(self,request,id=None):
        try:
            api_data=ApiData.objects.get(id=id)
            api_data.delete()
            
        except ApiData.DoesNotExist:
            return Response({'error : ':'This todo item does not exist.'},status=400)
        
        return Response(status=204)