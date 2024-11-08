from django.urls import path
from .views import create_order
from payment.views import PaymeCallBackAPIView
urlpatterns = [
    # path('paycom/', TestView.as_view()),
    path('create_order/', create_order, name='create_order'),
    # path('create_order/', PaymeCallBackAPIView.as_view, name='create_order'),

    # path('get_order/<str:code>/', get_order, name='get_order'),
]
