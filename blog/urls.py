from django.contrib import admin
from django.urls import path
from core.views import asosiy
from core.views import mevalar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('meva/', mevalar),
    
]
