from django.db import models

class BaseModel(models.Model):
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 


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
    logo_dark = models.ImageField(upload_to="logo/photo",verbose_name="Dark mode uchun logo ")
    logo_light = models.ImageField(upload_to="logo/photo",verbose_name="Dark mode uchun logo ")
    phone= models.CharField(max_length=13)


class Category(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    title = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to="Service/photo",   verbose_name='Servis  ikon kiriting')
    photo = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting')
    photo1 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo2 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo3 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo4 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    client_name = models.CharField(max_length=100)
    client_name_ru = models.CharField(max_length=100, null=True, blank=True)
    client_name_en = models.CharField(max_length=100, null=True, blank=True)
    client_description = models.TextField()
    client_description_ru = models.TextField(null=True, blank=True)
    client_description_en = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio rasmini kiriting')
    photo1 = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo2 = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo3 = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo4 = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    photo5 = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    category_id = models.ForeignKey(Category,verbose_name="Kategoriyani tanlang", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

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

    

