from rest_framework import serializers
from .models import Category, Contact, Text, About_image, Porfolio, Client, Social, Navbar, Slider, Client_about, \
    Register,SubCategory
from rest_framework.validators import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'icon')

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

    


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'title', 'title_ru', 'title_en', 'description', 'description_ru', 'description_en')


from rest_framework import serializers
from .models import Porfolio


class PorfolioSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Porfolio
        fields = ('id', 'category_id', 'name', 'client_name', 'about_project','problems','our_solution', 'photos')

    def get_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.name_en
        elif lang == 'ru':
            return obj.name_ru
        return obj.name

    def get_category_name(self, obj):
        lang = self.context.get('lang', 'uz')  # Lang parametri olish
        if lang == 'en':
            return obj.category_id.name_en
        elif lang == 'ru':
            return obj.category_id.name_ru
        else:
            return obj.category_id.name
        
    def get_category_description(self,obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.category_id.description_en
        elif lang == 'ru':
            return obj.category_id.description_ru
        else:
            return obj.category_id.description

    def get_client_name(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.client_name_en
        elif lang == 'ru':
            return obj.client_name_ru
        return obj.client_name


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

        
    def to_representation(self, instance):
        lang = self.context.get('lang', 'uz')  # Lang parametri olish
        data = super().to_representation(instance)
        data['name'] = getattr(instance, f'name_{lang}', instance.name)
        data['client_name'] = self.get_client_name(instance)
        data['about_project'] = getattr(instance, f'about_project_{lang}', instance.about_project)
        data['problems'] = getattr(instance, f'problems_{lang}', instance.problems)
        data['our_solution'] = getattr(instance, f'our_solution_{lang}', instance.our_solution)
        data['category_name'] = self.get_category_name(instance)
        data['category_description'] = self.get_category_description(instance)

        return data
    def get_category(self, obj):
        return obj.category.name
    
class SubCategorySerializer(serializers.ModelSerializer):
    sub_photo = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ('id', 'subcat_title', 'sub_description', 'sub_description1', 'sub_photo')

    def get_sub_photo(self, instance):
        sub_photo = [
            instance.sub_photo.url if instance.sub_photo else None,
            instance.sub_photo1.url if instance.sub_photo1 else None,
            instance.sub_photo2.url if instance.sub_photo2 else None,
            instance.sub_photo3.url if instance.sub_photo3 else None,
            instance.sub_photo4.url if instance.sub_photo4 else None,
        ]
        return sub_photo

    def to_representation(self, instance):
        lang = self.context.get('lang', 'uz')
        data = super().to_representation(instance)

        data['subcat_title'] = getattr(instance, f'subcat_title_{lang}', instance.subcat_title)
        data['sub_description'] = getattr(instance, f'sub_description_{lang}', instance.sub_description)
        data['sub_description1'] = getattr(instance, f'sub_description1_{lang}', instance.sub_description1)
        
        return data









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
