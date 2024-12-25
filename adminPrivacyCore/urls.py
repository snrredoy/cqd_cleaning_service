from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('showPrivacyCore/', views.showPrivacyCore, name="showPrivacyCore"),
    path('updatePrivacyCore/<int:pk>/', views.updatePrivacyCore, name="updatePrivacyCore"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)