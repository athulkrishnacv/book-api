from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to="books/images/")
    genre = models.ForeignKey("books.Genre",on_delete=models.CASCADE)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "books_book"

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "books_genre"
        verbose_name_plural = "genres"
    
    def __str__(self):
        return  self.name
    

class Covers(models.Model):
    name = models.ForeignKey("books.Book",on_delete=models.CASCADE)
    images = models.ImageField(upload_to="books/images/")

    class Meta:
        db_table = "books_cover"
        verbose_name_plural = "covers"

    def __str__(self):
        return  str(self.id)

        


    
