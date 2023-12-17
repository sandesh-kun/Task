from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from shop.views import product_list  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),  
    path('shop/', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)