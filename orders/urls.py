from django.urls import path
from .views import CreateOrderView, OrderListView, OrderStatusUpdateView, CheckoutView

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),                 # /api/orders/
    path('create/', CreateOrderView.as_view(), name='order-create'),      # /api/orders/create/
    path('checkout/', CheckoutView.as_view(), name='checkout'),           # /api/orders/checkout/
    path('<int:pk>/status/', OrderStatusUpdateView.as_view(), name='order-status-update'),
]
