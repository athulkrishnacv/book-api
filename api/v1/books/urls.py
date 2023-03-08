from django.urls import path
from api.v1.books.views import books, book, protected
urlpatterns = [
    path('',books),
    path('view/<int:pk>/',book),
    path('secure/<int:pk>/',protected),
] 
 