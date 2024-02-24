from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from polls import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.h1,name='home'),


    path('polls/',include('polls.urls')),
    path("admin/", admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)