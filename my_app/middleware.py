# middleware.py
from django.urls import resolve
from .models import Visitor


class SaveVisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # View pathini olish
        current_url_name = resolve(request.path_info).url_name

        # Admin va boshqa istalmagan URL larni tekshirish
        if current_url_name != 'admin' not in request.path:
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
            if ip_address:
                ip_address = ip_address.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            if not Visitor.objects.filter(ip_address=ip_address).exists():
                Visitor.objects.create(ip_address=ip_address)

        response = self.get_response(request)
        return response
