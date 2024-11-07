from django.urls import path
from .views import TestView, create_order, get_order

urlpatterns = [
    path('paycom/', TestView.as_view()),
    path('create_order/', create_order, name='create_order'),
    path('get_order/<str:code>/', get_order, name='get_order'),
]
