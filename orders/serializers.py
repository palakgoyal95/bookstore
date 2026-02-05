from rest_framework import serializers
from .models import Order, OrderItem
from books.models import Book
class OrderItemSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = OrderItem
        fields = ['book', 'book_title', 'quantity', 'price']
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'payment_status', 'items', 'created_at']
        read_only_fields = ['user', 'status', 'payment_status']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            book = item['book']
            quantity = item['quantity']

            if book.stock_quantity < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for {book.title}"
                )

            book.stock_quantity -= quantity
            book.save()

            OrderItem.objects.create(
                order=order,
                book=book,
                quantity=quantity,
                price=book.price
            )
        return order
