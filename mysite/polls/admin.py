from django.contrib import admin

# Register your models here.
from .models import MenuItem, Rating, Orders,Image23,Attendance,AT2,Menu,ExcelFile,ExcelData,Expenditure,Items,UserProfile
admin.site.register(MenuItem)
admin.site.register(Rating)
admin.site.register(Orders)
admin.site.register(Image23)
admin.site.register(Attendance)
admin.site.register(AT2)
admin.site.register(Menu)
admin.site.register(ExcelFile)
admin.site.register(ExcelData)
admin.site.register(Expenditure)
admin.site.register(Items)
admin.site.register(UserProfile)