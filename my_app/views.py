from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import Category, Contact, Text, About_image, Porfolio, Client, Social, Navbar, Slider, Client_about,SubCategory
from rest_framework import generics, permissions
from rest_framework import generics
import requests

from bs4 import BeautifulSoup

from django.http import HttpResponse
def render_site(request):
    try:
        response = requests.get("https://fargenius.vercel.app")
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')

            # Add a base tag to handle relative URLs
            base_tag = soup.new_tag('base', href='https://fargenius.vercel.app')
            soup.head.insert(0, base_tag)

            return HttpResponse(soup.prettify(), content_type='text/html')
        else:
            return HttpResponse("Failed to fetch the website content.", status=response.status_code)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

class CategoryView(APIView):
    def get(self, request, id=None, lang=None):
        try:
            if id is not None:
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category, context={'lang': lang})
            else:
                category = Category.objects.all()
                serializer = CategorySerializer(category, many=True, context={'lang': lang})
            return Response(serializer.data, status=200)  # Muvaffaqiyatli javobni 200 status kodi bilan qaytarish
        except Category.DoesNotExist:
            return Response({"error": "Category does not exist"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class NavbarView(APIView):
    def get(self, request):
        try:
            navbar = Navbar.objects.all()
            serializer = NavbarSerializer(navbar, many=True)
            return Response(serializer.data, status=200)  # Muvaffaqiyatli javobni 200 status kodi bilan qaytarish
        except Exception as e:
            return Response({"error": str(e)},
                            status=500)  # Barcha xato holatlar uchun 500 status kodi bilan xabar qaytarish


class SliderView(APIView):
    def get(self, request, lang=None):
        slider = Slider.objects.all()
        serializer = SliderSerializer(slider, many=True, context={'lang': lang})
        return Response(serializer.data)


class AboutView(APIView):
    def get(self, request, lang=None):
        about = About_image.objects.all()
        serializer = About_imageSerializer(about, many=True, context={'lang': lang})
        return Response(serializer.data)


class PortfolioView(APIView):
    def get(self, request, id=None, lang=None):
        if id is not None:
            portfolio = Porfolio.objects.filter(id=id)
        else:
            portfolio = Porfolio.objects.all()

        serializer = PorfolioSerializer(portfolio, many=True, context={'lang': lang})
        return Response(serializer.data)


class Category_about(APIView):
    def get(self, request, id=None, lang=None):


        category = Category.objects.filter(id=id)
        subcategories = SubCategory.objects.filter(subcat=id) if id else SubCategory.objects.all()
        subcategory_serializer = SubCategorySerializer(subcategories, many=True, context={'lang': lang})
        category_serializer = CategorySerializer(category, many=True, context={'lang': lang})        
        response_data = {
            'category_info':category_serializer.data,
            'subcategories': subcategory_serializer.data
        }
        return Response(response_data)


class ClientAboutView(APIView):
    def get(self, request, lang=None):
        client_about = Client_about.objects.all()
        serializer = Client_aboutSerializer(client_about, many=True, context={'lang': lang})
        return Response(serializer.data)



class PortfolioFilter(APIView):
    def get(self, request, id=None, lang=None):
        if id is not None:
            portfolio = Porfolio.objects.filter(category_id=id)
        else:
            portfolio = Porfolio.objects.all()
        serializer = PorfolioSerializer(portfolio, many=True, context={'lang': lang})
        return Response(serializer.data)

class PortfolioFilter1(APIView):
    def get(self, request, id=None, lang=None):
        if id is not None:
            portfolio = Porfolio.objects.filter(category_id=id)
        else:
            portfolio = Porfolio.objects.all()
        serializer = PorfolioSerializer(portfolio, many=True, context={'lang': lang})
        return Response(serializer.data)



class ContactView(APIView):
    def get(self, request, lang=None):
        try:
            contact = Contact.objects.all()
            serializer = ContactSerializer(contact, many=True, context={'lang': lang})
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                # Ma'lumotlarni olish
                name = serializer.validated_data['name']
                phone = serializer.validated_data['phone_num']
                service = serializer.validated_data['service']

                # Telegram bot uchun ma'lumotlar
                bot_token = '7001416771:AAFejGsntzCr-rXKwGqcdNIFcVCsVMFjR2Q'
                chat_id = '1327096215'  # Telegram botning chat_id sini o'zgartiring
                text = f"Saytdan xabar:\n\nIsmi: {name}\nTel: {phone}\nService: {service}"

                # Telegram bot orqali xabar jo'natish
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}'
                requests.get(url)
                return Response({'succes':True}, status=201)
            return Response({'succes':False}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
