from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Shibchar Express Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Shibchar Express Index"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
