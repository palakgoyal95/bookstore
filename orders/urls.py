from django.urls import path
from .views import CreateOrderView, OrderListView, OrderStatusUpdateView

urlpatterns = [
    path('', OrderListView.as_view()),                 # /api/orders/
    path('create/', CreateOrderView.as_view()),        # /api/orders/create/
    path('<int:pk>/status/', OrderStatusUpdateView.as_view()),
]
