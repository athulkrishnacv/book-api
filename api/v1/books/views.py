from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from books.models import Book
from api.v1.books.serializers import BookSerializer, BookDetailSerializer
from django.db.models import Q


@api_view(["GET"])
@permission_classes([AllowAny])

def books(request):
    instances =  Book.objects.filter(is_deleted = False)

    q = request.GET.get("q")

    if q:
        instances = instances.filter(Q(name__icontains=q) | Q(author_name__icontains=q))

    context = {
        "request" :  request
    }
    serializer = BookSerializer(instances,many =True,context=context)
    response_data = {
        "status_code" : 6000,
        "data" :  serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def book(request,pk):
    if Book.objects.filter(pk=pk).exists():
        instance = Book.objects.get(pk=pk)
        context = {
        "request" :  request
        }
   
        serializer = BookDetailSerializer(instance,context=context)
        response_data = {
            "status_code" : 6000,
            "data" :  serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6001,
            "message" :  "This Book doesn't exist"
        }
        return Response(response_data) 
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected(request,pk):
    if Book.objects.filter(pk=pk).exists():
        instance = Book.objects.get(pk=pk)
        context = {
        "request" :  request
        }
   
        serializer = BookDetailSerializer(instance,context=context)
        response_data = {
            "status_code" : 6000,
            "data" :  serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6001,
            "message" :  "This Book doesn't exist"
        }
        return Response(response_data) 

     

 
