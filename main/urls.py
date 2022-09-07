from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('edited',views.edited,name="edited"),
    path('accounts/profile/',views.home,name="home"),
    path('', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),
]
