from rest_framework import generics
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from accounts.permissions import IsAdmin, IsCustomer
class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsCustomer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return Order.objects.all()
class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.status = request.data.get('status')
        order.save()
        return Response({'message': 'Order status updated'})

