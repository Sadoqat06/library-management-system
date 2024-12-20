from rest_framework.views import APIView
from .models import BookOrder
from .serializers import BookOrderModelSerializer, BookOrderCreateSerializer, BookOrderUpdateSerializer
from rest_framework.response import Response
from rest_framework import status


class BookOrderModelGetView(APIView):

    def get(self,request):
        bkor = BookOrder.objects.all()
        bkorserializer = BookOrderModelSerializer(bkor,many = True)
        return Response(bkorserializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk,  *args, **kwargs):
        try:
           bko =  BookOrder.objects.get(pk = pk)
        except BookOrder.DoesNotExist:
            return Response({"Error":"Model not found "}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookOrderUpdateSerializer(bko, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Changed Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,  *args, **kwargs):
        try:
           bko =  BookOrder.objects.get(pk = pk)
        except BookOrder.DoesNotExist:
            return Response({"Error":"Model not found "}, status.HTTP_404_NOT_FOUND)
        
        bko.delete()
        return Response({"message":"Deleted"}, status.HTTP_200_OK)
        


class BookOrderModelCreateView(APIView):

    def post(self,request,*args, **kwargs):
        serializer = BookOrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Created Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)