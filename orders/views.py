from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from accounts.permissions import IsAdmin, IsCustomer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CreateOrderView(generics.CreateAPIView):
    """
    Create a new order
    """
    serializer_class = OrderSerializer
    permission_classes = [IsCustomer]

    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=OrderSerializer,
        responses={
            201: OrderSerializer,
            400: 'Bad Request - Invalid data or insufficient stock',
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CheckoutView(generics.CreateAPIView):
    """
    Checkout - Create an order from cart items
    """
    serializer_class = OrderSerializer
    permission_classes = [IsCustomer]

    @swagger_auto_schema(
        operation_summary="Checkout and create order",
        operation_description="Create a new order from the cart. Provide book items with quantities.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['items'],
            properties={
                'items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'book': openapi.Schema(type=openapi.TYPE_INTEGER, description='Book ID'),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quantity to order'),
                        },
                        required=['book', 'quantity']
                    ),
                    description='List of items to order'
                ),
            },
        ),
        responses={
            201: openapi.Response(
                description="Order created successfully",
                schema=OrderSerializer
            ),
            400: 'Bad Request - Invalid data or insufficient stock',
            401: 'Unauthorized - Authentication required',
        },
        tags=['Orders']
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class OrderListView(generics.ListAPIView):
    """
    List all orders (Admin only)
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_description="Get list of all orders (Admin only)",
        responses={200: OrderSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Order.objects.all()
class OrderStatusUpdateView(generics.UpdateAPIView):
    """
    Update order status (Admin only)
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_description="Update order status (Admin only)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'status': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=['PENDING', 'SHIPPED', 'DELIVERED'],
                    description='New order status'
                ),
            },
            required=['status']
        ),
        responses={
            200: openapi.Response(
                description="Status updated successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'message': openapi.Schema(type=openapi.TYPE_STRING)}
                )
            )
        }
    )
    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.status = request.data.get('status')
        order.save()
        return Response({'message': 'Order status updated'})

