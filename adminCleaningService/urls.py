from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('showCleaningService/', views.showCleaningService, name='showCleaningService'),
    path('updateCleaningServiceHeadding/<int:pk>/', views.updateCleaningServiceHeadding, name='updateCleaningServiceHeadding'),
    path('updateCleaningService/<int:pk>/', views.updateCleaningService, name='updateCleaningService'),
    path('deleteCleaningService/<int:pk>/', views.deleteCleaningService, name='deleteCleaningService'),
    path('addCleaningService/', views.addCleaningService, name='addCleaningService'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)