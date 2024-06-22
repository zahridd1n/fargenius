from django.contrib import admin

from .models import Category,Contact,Text,About_image,Porfolio,Client,Social,Navbar,Slider,Client_about,Register

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','title','description','icon')



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('description','image1','image2')


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')



@admin.register(About_image)
class About_imageAdmin(admin.ModelAdmin):
    list_display = ('image1', 'image2', 'description')
    list_display_links = ('description',)


@admin.register(Porfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name','description','client_name','client_description','photo','photo1','photo2','photo3','photo4','photo5')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','photo')

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name','link')

@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('phone','logo_dark','logo_light')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','description')


@admin.register(Client_about)
class Client_aboutAdmin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name','phone_num','service')