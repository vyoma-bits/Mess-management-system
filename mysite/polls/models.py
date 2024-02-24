

# Create your models here.

# Create your models here.
from django.db import models
from django.core.files.storage import FileSystemStorage

class MenuItem(models.Model):
    date = models.DateField( null=True )
    item = models.CharField(max_length=255)
   
    total_rating = models.IntegerField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    def __str__(self):
        return self.item


class Rating(models.Model):
    menu_item = models.CharField(max_length=90)
    rating = models.IntegerField(default="0")
    person = models.IntegerField(default="0")
    avg = models.IntegerField(default="0")
  



class Orders(models.Model):
    image=models.ImageField(upload_to='feedback_images/', null=True, blank=True)
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default=".")
class Image23(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE,null=True)

    content = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='myimage', storage=FileSystemStorage(),null=True)


from django.contrib.auth.models import User

class Attendance(models.Model):
    student = models.CharField(max_length=250,null=True)
    Dinner = models.CharField(max_length=20,default="0")
    breakfast = models.CharField(max_length=20,default="0")
    lunch = models.CharField(max_length=20,default="0") # Options: 'breakfast', 'lunch', 'dinner'

    def __str__(self):
        return self.student
class AT2(models.Model):
    date=models.CharField(max_length=20,default="0")
    Dinner = models.CharField(max_length=20,default="0")
    breakfast = models.CharField(max_length=20,default="0")
    lunch = models.CharField(max_length=20,default="0")
class Menu(models.Model):
    date=models.CharField(max_length=350)
    breakfast=models.CharField(max_length=350)
    dinner=models.CharField(max_length=350)
    lunch=models.CharField(max_length=350)
class ExcelFile(models.Model):
    file = models.FileField(upload_to='static')
class ExcelData(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()
class Expenditure(models.Model):
    name=models.CharField(max_length=350)
    exp=models.CharField(max_length=350,default="0")
class Items(models.Model):
    date = models.CharField( max_length=255,default=".")
    item1 = models.CharField(max_length=255,default=".")
    item2 = models.CharField(max_length=255,default=".")
    item3 = models.CharField(max_length=255,default=".")
    item4 = models.CharField(max_length=255,default=".")
    item5 = models.CharField(max_length=255,default=".")
    item6 = models.CharField(max_length=255,default=".")
    item7 = models.CharField(max_length=255,default=".")
    item8 = models.CharField(max_length=255,default=".")
    item9 = models.CharField(max_length=255,default=".")
    item10 = models.CharField(max_length=255,default=".")
    item11 = models.CharField(max_length=255,default=".")
    item12 = models.CharField(max_length=255,default=".")
    item13 = models.CharField(max_length=255,default=".")
    item14 = models.CharField(max_length=255,default=".")
    item15 = models.CharField(max_length=255,default=".")
    item16 = models.CharField(max_length=255,default=".")
    item17 = models.CharField(max_length=255,default=".")
    item18 = models.CharField(max_length=255,default=".")
    item19 = models.CharField(max_length=255,default=".")
    item19 = models.CharField(max_length=255,default=".")
    item20 = models.CharField(max_length=255,default=".")
    item21 = models.CharField(max_length=255,default=".")
    item22 = models.CharField(max_length=255,default=".")
    item23 = models.CharField(max_length=255,default=".")
    item24 = models.CharField(max_length=255,default=".")
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20) 





