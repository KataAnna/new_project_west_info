from django.db import models

from django.contrib.auth.models import User
#from django.db import models
#from django.contrib.sites.models import Site

from django.utils.safestring import mark_safe
from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer

class Customer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    
       
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, default='')
    #describe = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

class Company(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, default='')
    describe = models.TextField(default='')
    city = models.CharField(max_length=250, default='')
    address = models.TextField(default='')
    phone = models.CharField(max_length=250, default='')
    email = models.EmailField(unique=True)
    image = ImageCropField(upload_to='product', null=True, blank=True)

    cropping = ImageRatioField('image', '150x150')

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="%s" />' % self.image.url)
        except:
            return 'None'

    @property
    def get_small_image(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_url)

    @property
    def get_small_image_url(self):
        return BASE_URL + get_thumbnailer(self.image).get_thumbnail({
            'size': (100, 100),
            'box': self.cropping,
            'crop': 'smart',
        }).url

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class ReqOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    ammount = models.IntegerField(default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

'''class StaticFlatPage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70, blank=True)
    registration_required = models.BooleanField()
    sites = models.ManyToManyField(Site)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FlatPage'
        verbose_name_plural = 'FlatPages'
'''