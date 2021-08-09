from django.contrib import admin
from django.urls import path
from account import views
from main import views
#from account.views import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = 'main'),
    path('goods/', include('goods.urls')),
    path('account/', include('account.urls')),
]
