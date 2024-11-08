from my_app.models import Order
from payme.types import response
from payme.models import PaymeTransactions
from payme.views import PaymeWebHookAPIView


class PaymeCallBackAPIView(PaymeWebHookAPIView):
    
    
    def check_perform_transaction(self, params):
            account = self.fetch_account(params)
            self.validate_amount(account, params.get('amount'))
            result = response.CheckPerformTransaction(allow=True)
            item = response.Item(
                discount="10000",
                title="Joy Band Qilish Uchun ",
                price="50000000",
                count=1,
                code="00702001001000001",
                units="241092",
                vat_percent="15",
                package_code="123456"
            )
            result.add_item(item)
            return result.as_resp()


    def handle_created_payment(self, params, result, *args, **kwargs):

        print(f"Transaction created for this params: {params} and cr_result: {result}")

    def handle_successfully_payment(self, params, result, *args, **kwargs):

        transaction = PaymeTransactions.get_by_transaction_id(
            transaction_id=params["id"]
        )
        Order.mark_as_paid(order_id=transaction.account.id)



    def handle_cancelled_payment(self, params, result, *args, **kwargs):

        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")