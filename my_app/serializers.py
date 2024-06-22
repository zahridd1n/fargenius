from rest_framework import serializers
from .models import Category, Contact, Text, About_image, Porfolio, Client, Social, Navbar, Slider, Client_about, \
    Register
from rest_framework.validators import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'title', 'description', 'icon', 'photos')

    def get_name(self, obj):
        lang = self.context.get('lang', 'uz')
        print(lang, 'salom')
        # lang = request.query_params.get('lang', 'uz')  # default til - o'zbekcha
        if lang == 'en':
            return obj.name_en
        elif lang == 'ru':
            return obj.name_ru
        return obj.name

    def get_title(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.title_en
        elif lang == 'ru':
            return obj.title_ru
        return obj.title

    def get_description(self, obj):
        lang = self.context.get('lang', )
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        return obj.description

    def get_photos(self, instance):
        photos = [
            instance.photo.url if instance.photo else None,
            instance.photo1.url if instance.photo1 else None,
            instance.photo2.url if instance.photo2 else None,
            instance.photo3.url if instance.photo3 else None,
            instance.photo4.url if instance.photo4 else None,
        ]
        return photos


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'title', 'title_ru', 'title_en', 'description', 'description_ru', 'description_en')


from rest_framework import serializers
from .models import Porfolio


class PorfolioSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    client_description = serializers.SerializerMethodField()

    class Meta:
        model = Porfolio
        fields = ('id', 'category_id', 'name', 'description', 'client_name', 'client_description', 'photos')

    def get_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.name_en
        elif lang == 'ru':
            return obj.name_ru
        return obj.name

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        return obj.description

    def get_client_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.client_name_en
        elif lang == 'ru':
            return obj.client_name_ru
        return obj.client_name

    def get_client_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.client_description_en
        elif lang == 'ru':
            return obj.client_description_ru
        return obj.client_description

    def get_photos(self, instance):
        photos = [
            instance.photo.url if instance.photo else None,
            instance.photo1.url if instance.photo1 else None,
            instance.photo2.url if instance.photo2 else None,
            instance.photo3.url if instance.photo3 else None,
            instance.photo4.url if instance.photo4 else None,
            instance.photo5.url if instance.photo5 else None,
        ]
        return photos

    def get_category(self, obj):
        return obj.category.name


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'title1', 'title2', 'image1', 'image2')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'name', 'link')


class NavbarSerializer(serializers.ModelSerializer):
    socials = serializers.SerializerMethodField()

    class Meta:
        model = Navbar
        fields = ('logo_dark', 'logo_light', 'phone', 'socials')

    def get_socials(self, obj):
        social = Social.objects.all()
        return SocialSerializer(social, many=True).data


class SliderSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Slider
        fields = ('id', 'title', 'description')

    def get_title(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.title_en
        elif lang == 'ru':
            return obj.title_ru
        return obj.title

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        return obj.description


class About_imageSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = About_image
        fields = ('id', 'description', 'image1', 'image2')

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        return obj.description


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'photo')


class Client_aboutSerializer(serializers.ModelSerializer):
    clients = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Client_about
        fields = ('description', 'clients')

    def get_clients(self, obj):
        client = Client.objects.all()
        return ClientSerializer(client, many=True).data

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        return obj.description


class ContactSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ('description', 'image1', 'image2')

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        return obj.description


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('name', 'phone_num', 'service')
