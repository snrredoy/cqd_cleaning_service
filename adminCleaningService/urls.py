from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('showCleaningService/', views.showCleaningService, name='showCleaningService'),
    path('updateCleaningServiceHeadding/<int:pk>/', views.updateCleaningServiceHeadding, name='updateCleaningServiceHeadding'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)