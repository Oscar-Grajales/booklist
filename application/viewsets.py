from rest_framework import viewsets
from application.serializers import BooksSerializer
from application.models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer    