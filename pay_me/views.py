from django.shortcuts import render
from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from django.urls import path
from my_app.models import Order

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


