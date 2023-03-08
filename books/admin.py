from django.contrib import admin
from books.models import Book, Genre, Covers


class CoversAdmin(admin.TabularInline):
    list_display = ["id", "name"]
    model = Covers

    
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "author_name"]

    inlines = [CoversAdmin]

admin.site.register(Book,BookAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Genre,GenreAdmin)




