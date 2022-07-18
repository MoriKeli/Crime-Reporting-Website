from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = ''
admin.site.site_header = ''
admin.site.index_title = ''

urlpatterns = [
    path('', include('users.users_urls')),
    path('officials/', include('officers.officer_urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)