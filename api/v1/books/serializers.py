from rest_framework.serializers import ModelSerializer
from books.models import Book, Genre, Covers
from rest_framework import serializers


class BookSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "name", "author_name", "featured_image", "is_deleted")
        model = Book


class CoverSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "images")
        model = Covers


class BookDetailSerializer(ModelSerializer):

    genre = serializers.SerializerMethodField()
    covers = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "name", "is_deleted", "genre", "description", "covers")
        model = Book

    def get_genre(self, instance):
        return instance.genre.name
    
    def get_covers(self, instance):
        request = self.context.get("request")
        context= {
            "request": request
        }
        images = Covers.objects.filter(name=instance)
        serializer = CoverSerializer(images,many=True,context=context)
        return serializer.data



   
       