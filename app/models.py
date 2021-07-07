from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


# Create your models here.
class Property(models.Model):
    status = (
        ('re', 'Rent'),
        ('sa', 'Sale')
    )

    yes_no = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    

    name = models.CharField(null=False, blank=False, max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places=2, null=False, blank=False)
    city = models.CharField(null=False, blank=False, max_length=30)
    floor_plan = models.ImageField(upload_to ='uploads/')
    video = models.FileField(upload_to='uploads/', default="")
    image_1 = models.ImageField(upload_to ='uploads/')
    image_2 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_3 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_4 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_5 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_6 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_7 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_8 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_9 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    image_10 = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    bathroom = models.IntegerField(null=False)    
    address = models.CharField(max_length=100, null=False, blank=False)
    kitchen = models.IntegerField(null=False, blank=False)
    garage = models.IntegerField(null=False, blank=False)
    bedrooms = models.IntegerField(null=False, blank=False)
    sqft = models.IntegerField(null=False, blank=False)
    status = models.CharField(choices=status, max_length=10)
    date_built = models.DateField()
    balcony = models.IntegerField(null=False, blank=False)
    archive = models.BooleanField(default=False)
    parking = models.CharField(choices=yes_no, max_length=30)
    land_area = models.IntegerField(null=False, blank=False)
    property_lot_size = models.IntegerField(null=False, blank=False)
    size = models.IntegerField(null=False, blank=False)
    sold = models.BooleanField(default=False)
    # creation_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.name



class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Pending')
    creation_date = models.DateField(auto_now=True)

