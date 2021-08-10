from django.contrib import admin
# from accounts import views
from main import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = 'main'),
    path('goods/', include('goods.urls')),
    path('accounts/', include('accounts.urls')),
]
