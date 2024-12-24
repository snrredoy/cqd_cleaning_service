from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("addSubscriptionPackage/", views.addSubscriptionPackage , name="addSubscriptionPackage"),
    path("showSubscriptionPackage/", views.showSubscriptionPackage , name="showSubscriptionPackage"),
    path("updateSubscriptionPackage/<int:pk>/", views.updateSubscriptionPackage , name="updateSubscriptionPackage"),
    path("deleteSubscriptionPackage/<int:pk>/", views.deleteSubscriptionPackage , name="deleteSubscriptionPackage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)