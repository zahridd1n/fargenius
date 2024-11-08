from my_app.models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from payme import Payme
from sayt.settings import PAYME_ID

from payment.views import PaymeCallBackAPIView


payme = Payme(payme_id=PAYME_ID)


from decimal import Decimal

@api_view(['POST'])
def create_order(request):
    total = request.data.get('total')
    name = request.data.get('name')
    phone_number = request.data.get('phone_number')
    code = request.data.get('code')

    user = User.objects.get(username='Paycom')
    order = Order.objects.create(
        user=user,
        total=total,
        is_finished=False,
        name=name,
        phone_num=phone_number,
        code=code
    )

    total1 = int(order.total)
    url = payme.initializer.generate_pay_link(id=order.id, amount=total1, return_url=code)


    return Response({
        "message": "Order created successfully",
        'data': {
            'order_id': order.id,
            'code': order.code,
            'total': order.total,
            'name': order.name,
            'phone_number': order.phone_num,
            'is_finished': order.is_finished,
            'url': url,
        }
    })


