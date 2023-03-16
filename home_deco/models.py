from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class HomeDecoListing(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200)
    price_new = models.IntegerField(blank=True)
    price_old = models.IntegerField(blank=True)
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assembled_size =models.CharField(max_length=200)
    structured_frame = models.CharField(max_length=200)
    assembly = models.CharField(max_length=200)
    made_in_location = models.CharField(max_length=200)
    offer = models.CharField(max_length=200)
    photo_main =models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title