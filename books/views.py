from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from accounts.permissions import IsAdmin
from rest_framework.permissions import AllowAny
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'author']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [AllowAny()]
