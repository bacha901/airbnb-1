
from django.urls import path , include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('property/' , include('property.urls' , namespace='property')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('summernote/', include('django_summernote.urls')),
]


urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)