from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('showCQDAdvantage/', views.showCQDAdvantage, name="showCQDAdvantage"),
    path('updateCQDAdvantage/<int:pk>/', views.updateCQDAdvantage, name="updateCQDAdvantage"),
    path('deleteCQDAdvantage/<int:pk>/', views.deleteCQDAdvantage, name="deleteCQDAdvantage"),
    path('addCQDAdvantage/', views.addCQDAdvantage, name="addCQDAdvantage"),
    path('updateCQDAdvantageSection/<int:pk>/', views.updateCQDAdvantageSection, name="updateCQDAdvantageSection"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)