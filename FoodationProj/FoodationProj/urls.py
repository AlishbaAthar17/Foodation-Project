
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FoodationApp.urls')),
    path('api/', include('FoodationApp.api.urls'))
]
