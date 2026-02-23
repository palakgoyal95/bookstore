from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BookListCreateView(APIView):
    """
    GET  -> List all books (public)
    POST -> Add new book (admin only)
    """
    serializer_class = BookSerializer

    @swagger_auto_schema(
        operation_summary="List all books",
        operation_description="Get a list of all available books",
        responses={
            200: BookSerializer(many=True)
        },
        tags=['Books']
    )
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new book",
        operation_description="Add a new book to the store (Admin only)",
        request_body=BookSerializer,
        responses={
            201: BookSerializer,
            403: 'Forbidden - Admin access required',
            400: 'Bad Request - Invalid data'
        },
        tags=['Books']
    )
    def post(self, request):
        # Only admin can add books
        if not request.user.is_staff:
            return Response(
                {"detail": "Only admin can add books"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
