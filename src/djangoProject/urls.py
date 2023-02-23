from django.contrib import admin
from django.urls import path
from booking.views import index, event_detail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('event<int:id>', event_detail, name="event_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
