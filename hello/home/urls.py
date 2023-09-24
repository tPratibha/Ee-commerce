from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name="index"),
    path('Tshirt', views.Tshirt, name="Tshirt"),
    path('profile', views.profile, name="profile"),

]
