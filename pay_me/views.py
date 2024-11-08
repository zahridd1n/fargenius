from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
paycom = Paycom()
from django.urls import path
from my_app.models import Order


from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

class CheckOrder(Paycom):
    def check_order(self, amount: int, account: dict, *args, **kwargs):
        order = Order.objects.filter(id=account["order_id"], is_finished=False).first()

        if not order:
            return self.ORDER_NOT_FOND
        if order.total * 100 != amount:
            return self.INVALID_AMOUNT

        return self.ORDER_FOUND


    def successfully_payment(self, account: dict, transaction, *args, **kwargs):
        order = Order.objects.filter(id=transaction.order_key).first()

        if not order:
            return self.ORDER_NOT_FOND

        order.is_finished = True
        order.save()


    def cancel_payment(self, account, transaction, *args, **kwargs):
        print(account)

class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


@api_view(['POST'])
def create_order(request):
    # user_id = request.data.get('user')
    total = request.data.get('total')
    name = request.data.get('name')
    phone_number = request.data.get('phone_number')
    code = request.data.get('code')

    user = User.objects.get(username='Paycom')

    order = Order.objects.create(user=user, total=total, is_finished=False, name=name, phone_num=phone_number, code=code)
    url = paycom.create_initialization(amount=total, order_id=order.id, return_url='https://example.com/success/')
    # Bu yerda serializer orqali yoki to'g'ridan-to'g'ri response qaytarish mumkin
    return Response({"message": "Order created successfully",
                     'data':{
                         'order_id': order.id,
                         'code': order.code,
                         'total': order.total,
                         'name': order.name,
                         'phone_number': order.phone_num,
                         'is_finished': order.is_finished,
                         'url': url

                     }}
                    )

@api_view(['GET'])
def get_order(request, code):
    order = get_object_or_404(Order, code=code)
    serializer = serializers.OrderSerializer(order)
    return Response(serializer.data)
