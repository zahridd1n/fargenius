from django.db import models
import requests

class BaseModel(models.Model):
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Visitor(models.Model):
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    visit_datetime = models.DateTimeField(auto_now_add=True)

    @property
    def count(self):
        return Visitor.objects.filter().count()


class Slider(models.Model):
    title = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Navbar(BaseModel):
    logo_dark = models.ImageField(upload_to="logo/photo", verbose_name="Dark mode uchun logo ")
    logo_light = models.ImageField(upload_to="logo/photo", verbose_name="Dark mode uchun logo ")
    phone = models.CharField(max_length=13)


class Category(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to="Service/photo", verbose_name='Servis  ikon kiriting')
    icon_light = models.ImageField(upload_to="Service/photo", verbose_name="liGhT model uchun ikon")

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    subcat_title = models.TextField(null=True, blank=True)
    subcat_title_ru = models.TextField(null=True, blank=True)
    subcat_title_en = models.TextField(null=True, blank=True)
    sub_description = models.TextField(null=True, blank=True)
    sub_description_ru = models.TextField(null=True, blank=True)
    sub_description_en = models.TextField(null=True, blank=True)
    sub_description1 = models.TextField(null=True, blank=True)
    sub_description1_ru = models.TextField(null=True, blank=True)
    sub_description1_en = models.TextField(null=True, blank=True)
    sub_photo = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting')
    sub_photo1 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting', blank=True,
                                   null=True)
    sub_photo2 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting', blank=True,
                                   null=True)
    sub_photo3 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting', blank=True,
                                   null=True)
    sub_photo4 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting', blank=True,
                                   null=True)
    subcat = models.ForeignKey(Category, verbose_name='Qaysi categoriyaga oidligini kiriting', on_delete=models.CASCADE)

    def __str__(self):
        return self.subcat_title


class Text(BaseModel):
    title = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class About_image(BaseModel):
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="about/image1", verbose_name='About rasmini kiriting')
    image2 = models.ImageField(upload_to="about/image1", verbose_name='About rasmini kiriting')


class Porfolio(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name')
    name_ru = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name (Russian)')
    name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name (English)')
    client_name = models.CharField(max_length=100, verbose_name='Client Name')
    client_name_ru = models.CharField(max_length=100, null=True, blank=True, verbose_name='Client Name (Russian)')
    client_name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name='Client Name (English)')
    about_project = models.TextField(null=True, blank=True, verbose_name='About Project')
    about_project_ru = models.TextField(null=True, blank=True, verbose_name='About Project (Russian)')
    about_project_en = models.TextField(null=True, blank=True, verbose_name='About Project (English)')
    problems = models.TextField(null=True, blank=True, verbose_name='Problems')
    problems_ru = models.TextField(null=True, blank=True, verbose_name='Problems (Russian)')
    problems_en = models.TextField(null=True, blank=True, verbose_name='Problems (English)')
    our_solution = models.TextField(null=True, blank=True, verbose_name='Our Solution')
    our_solution_ru = models.TextField(null=True, blank=True, verbose_name='Our Solution (Russian)')
    our_solution_en = models.TextField(null=True, blank=True, verbose_name='Our Solution (English)')
    photo = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio Photo')
    photo1 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 1', blank=True, null=True)
    photo2 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 2', blank=True, null=True)
    photo3 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 3', blank=True, null=True)
    photo4 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 4', blank=True, null=True)
    photo5 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 5', blank=True, null=True)
    photo6 = models.ImageField(upload_to="portfolio/photo", blank=True, null=True)
    photo7 = models.ImageField(upload_to="portfolio/photo", blank=True, null=True)
    category_id = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)

    def get_category_name(self):
        return self.category_id.name


class Client_about(BaseModel):
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)


class Client(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="clients/photo", verbose_name='Portfolio rasmini kiriting')

    def __str__(self) -> str:
        return self.name


class Contact(BaseModel):
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="contact/photo", verbose_name='Portfolio rasmini kiriting')
    image2 = models.ImageField(upload_to="contact/photo", verbose_name='Portfolio rasmini kiriting')

    def __str__(self) -> str:
        return self.description


class Social(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Register(BaseModel):
    name = models.CharField(max_length=120)
    phone_num = models.CharField(max_length=13)
    service = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# ------------------------Payme uchun----------------------------------------

from decimal import Decimal

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_num = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    tarif = models.CharField(max_length=1000000, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - Total: {self.total}"
    
    @classmethod
    def mark_as_paid(cls, order_id):
        # Получаем заказ по ID
        order = cls.objects.get(id=order_id)
        
        # Устанавливаем is_finished в True
        order.is_finished = True
        order.save()
        
        # Если заказ завершен, отправляем данные в Bitrix24
        if order.is_finished:
            cls.send_to_bitrix24(order)

    @classmethod
    def send_to_bitrix24(cls, order):
        url = "https://idosmetov.bitrix24.kz/rest/24/yeh742klre4ckgpb/crm.lead.add.json"
        
        # Проверка и корректировка номера телефона
        
        # Если номер не начинается с +998, добавляем префикс +998
       

        # Данные для отправки в Bitrix24
        data = {
            'fields': {
                'TITLE': f"Yangi to'lov qilgan mijoz#",  # Название лида
                'NAME': order.name,  # Имя клиента
                'PHONE': [{'VALUE': order.phone_number, 'VALUE_TYPE': 'WORK'}],  # Телефон с правильным форматом
                'COMMENTS': f"Tarif: {order.tarif} buyurtma raqami {order.id}" ,  # Дополнительная информация
                'OPPORTUNITY': f"To'lov qilindi {order.total}",  # Сумма заказа
                'CURRENCY_ID': 'UZS',  # Валюта (UZS)
                'IS_OPENED': 'Y',  # Доступен для всех
                'SOURCE_ID': 'Restart Dosmedov saytidan',  # Дополнительно об источнике (не заполнено)
                'COMMENTS': "ushbu foydalanuvchi boshlangich tolovni amalga oshirdi",  # Комментарии (не заполнено)
            }
        }

        # Отправляем POST-запрос в Bitrix24
        response = requests.post(url, json=data)
        
        # Проверка ответа
        if response.status_code == 200:
            print('Лид успешно добавлен в Bitrix24:', response.json())
        else:
            print('Ошибка при добавлении лида в Bitrix24:', response.status_code, response.text)