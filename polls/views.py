from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from .models import MenuItem, Rating, Orders,Image23,Attendance,AT2,Menu,ExcelData,ExcelFile,Expenditure
from polls.models import Menu
from django.utils import formats
from social_django.models import UserSocialAuth
from datetime import datetime, timedelta
from math import ceil
# import the logging library
import logging
from django.db.models import Avg
import pandas 
import xlrd
from xlrd import open_workbook
import datetime
from datetime import datetime
import pandas as pd
import openpyxl
from django.core.files.storage import FileSystemStorage


from PIL import Image


now = datetime.now()


def login(request):
    return render(request,'login.html')

def h1(request):
    return render(request,'basic.html')
def home(request):
        current_time = datetime.now()

    # Identify the current student
    

    # Determine the upcoming meal
        next_meal = None
        if current_time.hour < 11:
            next_meal = 'breakfast'
        elif current_time.hour < 14:
            next_meal = 'lunch'
        elif current_time.hour <20:
            next_meal = 'dinner'
        else:
            next_meal = 'breakfastn1'
        
        today = datetime.today()
        
        
# Shift the date to the next day
        
        next_meal_menu=None
        tomorrow=today+timedelta(days=1)
        a=today.strftime("%Y-%m-%d")+" "
        b=tomorrow.strftime("%Y-%m-%d")+" "
       
        
        
        
        
        

        if next_meal == 'breakfast':
            next_meal_menu = Menu.objects.get(date=a).breakfast
        elif next_meal == 'lunch':
            next_meal_menu = Menu.objects.get(date=a).lunch
        elif next_meal == 'dinner':
            next_meal_menu = Menu.objects.get(date=a).dinner
        elif next_meal == 'breakfastn1':
            next_meal_menu = Menu.objects.get(date=b).breakfast
        a={}
        a["next_meal_menu"]=next_meal_menu
        a["next_meal"]=next_meal

        

        
        return render(request,'index.html',a)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login1')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            return redirect('staff_dashboard')
 
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login1.html')
def staff_dashboard(request):
    feedbacks = Image23.objects.all()

    menu_items = MenuItem.objects.all()
    average_ratings = menu_items.annotate(average_rating=Avg('rating'))

    context = {
        'feedbacks': feedbacks,
        'menu_items': menu_items,
        'average_ratings': average_ratings,
    }
    return render(request, 'st_dash2.html', context)
def menu_display(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu_display.html', {'menu_items': menu_items})

def rating1(request, menu_item_id):
    menu_item1 = MenuItem.objects.get(id=menu_item_id)
    if request.method == 'POST':
        address2=request.POST.get('address2','')
        image4 = request.FILES['image1']

        
        
       


        o=Image23(image=image4,menu_item=menu_item1,content=(address2))
        o.save()
    return render(request, 'rating.html', {'menu_item': menu_item1})




def checkout(request):
    if request.method=="POST":
        
      
        name = request.POST.get('name', '')
       
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
       
        order = Image23(content=city)
        order.save()
        thank = True
        id = order.order_id
        
    return render(request, 'checkout.html')
def mark_presence(request):
    if request.method=="POST":
        current_time = datetime.now()

        mess_timings = [
            (datetime.strptime('7:00 AM', '%I:%M %p'), datetime.strptime('9:00 AM', '%I:%M %p')),
            (datetime.strptime('12:00 PM', '%I:%M %p'), datetime.strptime('2:00 PM', '%I:%M %p')),
            (datetime.strptime('7:00 PM', '%I:%M %p'), datetime.strptime('9:00 PM', '%I:%M %p')),
        ]
        is_within_mess_hours = False
        for start_time, end_time in mess_timings:
    
            if start_time.strftime('%I:%M %p') <= current_time.strftime('%I:%M %p') <= end_time.strftime('%I:%M %p'):
                is_within_mess_hours = True
                break

        if not is_within_mess_hours:
            # Display an error message if the student is not marking during mess hours
            error_message = 'Attendance marking is only allowed during mess hours.'
            context = {'error_message': error_message}
            return render(request, 'dashboard.html', context)

        # Check if the student has already marked their attendance for the current meal
        # (Use student's attendance records to determine this)

        # If the student has not yet marked their attendance for the current meal,
        # mark their attendance and redirect them to the dashboard with a success message

        success_message = 'Attendance marked successfully.'
        stu=request.POST.get('use1')
        c=0
        for i in Attendance.objects.all():
                    if stu==i.student:
                        c=c+1
        if c==0:
            ar=Attendance(student=stu)
            ar.save()
     
                        
                    
                    
        


        
        meal_ti=request.POST.get('meal_time')
        att = Attendance.objects.get(student="admin")
        if meal_ti=="breakfast":
            att.breakfast=int(att.breakfast)+1
        if meal_ti=="lunch":
            att.lunch=int(att.lunch)+1
        if meal_ti=="dinner":
            att.Dinner=int(att.Dinner)+1
        att.save()

        

        

        context = {'success_message': success_message}
    

    return render(request, 'mark_presence.html')
def calculate_fees(request):
    # Get the attendance data for the student
    d1=Attendance.objects.all()

    k=0
    for i in d1:
        c=0
        for j in Expenditure.objects.all():
                    if i.student==j.name:
                        c=c+1
        if c==0:

           

            d2=Expenditure(name=i.student)
            d2.save()
        u=i.student
        ci=Expenditure()
        attendance_data = get_attendance_data(u)
        total_cost_breakfast =attendance_data[0] * 80
        total_cost_lunch = attendance_data[1] * 150
        total_cost_dinner =attendance_data[2] * 80


    # Calculate the total fees
        total_fees = total_cost_breakfast + total_cost_lunch + total_cost_dinner
        k=total_fees
        ty=Expenditure.objects.get(name=u)
        ty.exp=total_fees
        ty.save()


    
    
   
    

    
    

   
   


     #Calculate the total cost of breakfast, lunch, and dinner
    


    # Render the template with the student's fees
    return HttpResponse(k)

# Get the attendance data for the student
def get_attendance_data(student_id):
    # Get the attendance data from the database
    attendance_data = Attendance.objects.get(student=student_id)
    o=[]
    if len(attendance_data.breakfast)>=0:

        o.append(int(attendance_data.breakfast))
        o.append(int(attendance_data.lunch))
        o.append(int(attendance_data.Dinner))
    
    return o
def count(request):
    ad=AT2.objects.all()
    meal={}
    b1=0
    l1=0
    d1=0
    for i in ad:
        b1=b1+int(i.breakfast)
        l1=l1+int(i.lunch)
        d1=d1+int(i.Dinner)
    meal["breakfast"]=b1
    meal["lunch"]=l1
    meal["dinner"]=d1
    return render(request,'count.html',meal)
def get_next_meal_menu(request):
    # Retrieve the current time
    current_time = datetime.now()

    # Identify the current student
    

    # Determine the upcoming meal
    next_meal = None
    if current_time.hour < 11:
        next_meal = 'breakfast'
    elif current_time.hour < 14:
        next_meal = 'lunch'
    elif current_time.hour <20:
        next_meal = 'dinner'
    else:
        next_meal = 'breakfastn1'
    next_meal_menu = None
    today = datetime.today()
# Shift the date to the next day
    tomorrow = today - timedelta(days=1)
    if next_meal == 'breakfast':
        next_meal_menu = Menu.objects.get(date=formats.date_format(today, Menu._meta.get_field('date_field').format)).breakfast
    elif next_meal == 'lunch':
        next_meal_menu = Menu.objects.get(date=formats.date_format(today, Menu._meta.get_field('date_field').format)).lunch
    elif next_meal == 'dinner':
        next_meal_menu = Menu.objects.get(date=formats.date_format(today, Menu._meta.get_field('date_field').format)).dinner
    elif next_meal=="breakfastn1":
        next_meal_menu=Menu.objects.get(date=formats.date_format(tomorrow, Menu._meta.get_field('date_field').format)).breakfast
    return HttpResponse("next_meal_menu")


    return render(request,'index.html',{"next_meal_menu":next_meal_menu})
def remove(l):# function for removing empty spaces and * pattern
    p=[]
    for i in l:
        if( str(i) in "*****************" or str(i)=="nan"):
            pass
        else:
            p.append(i)
    return p



def pass_file(file):  # function for parsing the excel file
    df = pd.read_excel(file,header=1)
    l=[]
    a=[]
   

    for col in df.columns:
        
        a.append(col)
  
    for j in range(15):
        meals=[]

        for i, row in df.iterrows():
        
            meal = row[a[j]]
            meals.append(meal)
            
        l.append(meals)
   
    w=[]
    for y in range(15):# logic for the loop is that we slice the list till the contents of dinner,lunch,breakfast and then we remove the spaes or **** pattern
        
    
        
        o=l[y][23:29][:]
        d=remove(o)
        
        
        r=l[y][1:10][:]
        b=remove(r)
        
        c=l[y][12:20][:]
        t=remove(c)
        
       
            
      
       
        f=[{"Breakfast":b,"Lunch":t,"Dinner":d}]
       
        e=[str(a[y])[0:11]]
        e.append(f)
        w.append(e)
    return w
def extract(l):
    a=""
    for i in l:
        a=a+i
    return a
  

def menu_upload(request):
    file = 'static/Mess Menu.xlsx'
    meals = pass_file(file)
    for i in range(len(meals)):
        a=meals[i][0]
        a.strip()



    
        mk=Menu(date=a,breakfast=extract(meals[i][1][0].get('Breakfast')),lunch=extract(meals[i][1][0].get('Lunch')),dinner=extract(meals[i][1][0].get('Dinner')))
        mk.save()
    return HttpResponse("hi")
def google_name(request):
    
    if True:
        # Get the current user
        user1 =request.POST.get('user')
        # Retrieve the Google name from the UserSocialAuth object
        user_social_auth = UserSocialAuth.objects.get(user=14)
        google_name = user_social_auth.extra_data['auth_time']
        return HttpResponse(google_name)
    else:
        return HttpResponse("madarchod")
def upload_image(request):
    if request.method == 'POST':
        # Get the image file from the request
        image_file = request.FILES['image']
        nam1e = request.POST['name']
       


        # Open the image file as an Image object
        
        a=Image23(image=image_file,content=nam1e)
        a.save()

        # Return the image data as an HTTP response
        return HttpResponse("jnjn")
    else:
        # Render the upload form HTML
        return render(request, 'upload_image.html')
def save_excel_file_data(excel_file):
    # Load the Excel file
    workbook = openpyxl.load_workbook(excel_file.file)

    # Get the first worksheet in the workbook
    worksheet = workbook.worksheets[0]

    # Iterate through the rows and columns of the worksheet
    for row in worksheet.iter_rows(min_row=2):
        # Create a new instance of the ExcelData model
        excel_data = ExcelData()

        # Set the data fields based on the values in the current row
        excel_data.name = row[0].value
        excel_data.value = row[1].value

        # Save the ExcelData instance to the database
        excel_data.save()
def upload_excel_file(request):
    if request.method == 'POST':
        # Get the uploaded Excel file
        excel_file = request.FILES['excel_file']

        # Save the Excel file to the media directory using FileSystemStorage
        fs = FileSystemStorage()
        filename = fs.save('static/' + excel_file.name, excel_file)

        # Create an ExcelFile instance with the saved filename
        saved_excel_file = ExcelFile(file=filename)

        # Save the ExcelFile instance to the database
        saved_excel_file.save()

        # Save the Excel file data to the database
        

        # Return a success message
        return HttpResponse('Excel file uploaded and processed successfully.')
    else:
        # Render the upload form HTML
        return render(request, 'upload_excel.html')
def data3(request):
    return render(request,"download_data.html")

from django.http import HttpResponse
from django.shortcuts import render
import xlsxwriter
from django.http import FileResponse
from django.conf import settings
import os

def data(request):
   
    file=os.path.join(settings.BASE_DIR,'Mess Menu.xlsx')
    fileopened=open(file,'rb')
    return FileResponse(fileopened)

def data1(request):
    return render(request,"data1.html")
def hi(request):
    file=os.path.join(settings.BASE_DIR,'Mess Menu.xlsx')
    fileopened=open(file,'rb')
    return FileResponse(fileopened)
def index1(request):
    return render(request,"index.html")
def start(request):
    return render(request,"staff2.html")
def expenditure(request):
    ER=Expenditure.objects.all()
    a=0
    h=0
    for i in ER:
        h=h+1
        a=int(i.exp)+a

    FT=AT2.objects.all()
    FTE=Rating.objects.all()
    
    for i in FTE:
        i.avg=i.rating/i.person
        i.save()
        
    
   

   
    

    
    

    return render(request,"staff2.html",{"ER":ER,"FT":FT,"a":a,"h":h,"FTE":FTE})
def time(request):
    FT=AT2.objects.all()
    return render(request,"staff2.html",{"FT":FT})
def ju(request):
        file=os.path.join(settings.BASE_DIR,'WIN_20231025_23_08_19_Pro_wKP65t0.jpg')
        fileopened=open(file,'rb')
        return FileResponse(fileopened)






    
    

    
    








        
    

