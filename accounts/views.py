from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers

User = get_user_model()

@swagger_auto_schema(
    method='post',
    operation_summary="Register a new user",
    operation_description="Create a new user account",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'password'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
        },
    ),
    responses={
        200: openapi.Response(
            description="User registered successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'message': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        ),
        400: 'Bad Request - Missing fields or user already exists'
    },
    tags=['Authentication']
)
@extend_schema(
    request=inline_serializer(
        name='RegisterRequest',
        fields={
            'username': serializers.CharField(),
            'password': serializers.CharField(),
            'email': serializers.EmailField(required=False),
        },
    ),
    responses={
        200: inline_serializer(
            name='RegisterResponse',
            fields={'message': serializers.CharField()}
        ),
        400: inline_serializer(
            name='RegisterErrorResponse',
            fields={'error': serializers.CharField()}
        ),
    },
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    return Response({'message': 'User registered successfully'})

@swagger_auto_schema(
    method='get',
    operation_summary="Test JWT authentication",
    operation_description="Test endpoint to verify JWT authentication is working",
    responses={
        200: openapi.Response(
            description="Authentication successful",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={'message': openapi.Schema(type=openapi.TYPE_STRING)}
            )
        ),
        401: 'Unauthorized - Invalid or missing token'
    },
    tags=['Authentication']
)
@extend_schema(
    responses={
        200: inline_serializer(
            name='ProtectedSuccessResponse',
            fields={'message': serializers.CharField()}
        ),
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_protected(request):
    return Response({"message": "JWT authentication successful 🎉"})
