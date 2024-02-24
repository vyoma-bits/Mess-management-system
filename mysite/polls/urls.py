from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from polls import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('login/',views.login1,name='login'),
    path('home',views.home,name='dashboard'),
    path('',views.h1,name='home'),
    path('feedback/', views.checkout, name='feedback'),
    path('rating', views.rating1, name='rating1'),
    path('menu/', views.menu_display, name='menu_display'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('checkout/', views.checkout,name="Checkout"),
    path('mark_presence',views.mark_presence,name="mark_presence"),
    path('calculate_fees/', views.calculate_fees, name='calculate_fees'),
    path('calculate_attendance/', views.get_attendance_data, name='calculate_feees'),
    path('count',views.count,name='count'),
    path('next',views.get_next_meal_menu,name='dt'),
    path('menu_upload',views.menu_upload,name='dtfs'),

    path('RT',views.rating1,name='naDDme'),
    path('up',views.upload_image,name='naDDme'),
    path('down',views.upload_excel_file,name='naDDme'),
    path('data3',views.data3,name='download'),
    path('Mess Menu234.xlsx',views.hi,name="dw"),
    path('data',views.data,name='downluoad'),
    path('index',views.index1,name='downljhuoad'),
    path('staff2',views.start,name='downljkhuoad'),
    path('Exp',views.expenditure,name='downljhuodad'),
    path('time',views.time,name='downlhhjhuordad'),
    path('WIN_20231025_23_08_19_Pro_wKP65t0.jpg',views.ju,name="dd"),
    path('uio',views.uio,name='downlhhhjhuordad'),
    path('send',views.send,name='downlhhdffashjhuordad'),
    path('profile',views.profile,name='downlhhdashjhuordad'),
    path('menu_up1',views.menu_up1,name='dowdsnlhhdashjhuordad'),
    path('data2',views.data2,name='data2'),
    path('data28',views.view_name,name='data2'),
    path('data5',views.data,name='down5luoad'),
    path('Expenditure.xlsx',views.hi1,name="dw5"),
    path('menu_process',views.menu_process,name="menu_process"),
    path('logout',views.logout1,name="logout1"),




    path('sign/',views.LoginPage,name='ss'),
    path('login1/',views.LoginPage,name='login1'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)








