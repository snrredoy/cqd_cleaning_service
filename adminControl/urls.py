from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.dashboard , name="dashboard"),
    path("update/<int:pk>/", views.updateGeneralSetting , name="updateGeneralSetting"),

    path("addTrustedPartner/", views.addTrustedPartner , name="addTrustedPartner"),
    path("showTrustedPartners/", views.showTrustedPartners , name="showTrustedPartners"),
    path("updateTrustedPartner/<int:pk>/", views.updateTrustedPartner , name="updateTrustedPartner"),
    path("deleteTrustedPartner/<int:pk>/", views.deleteTrustedPartner , name="deleteTrustedPartner"),

    path("addCommercialServices/", views.addCommercialServices , name="addCommercialServices"),
    path("showCommercialServices/", views.showCommercialServices , name="showCommercialServices"),
    path("updateCommercialServices/<int:pk>/", views.updateCommercialServices , name="updateCommercialServices"),
    path("deleteCommercialServices/<int:pk>/", views.deleteCommercialServices , name="deleteCommercialServices"),

    path("showInteractivePlatform/", views.showInteractivePlatform , name="showInteractivePlatform"),
    path("updateInteractivePlatform/<int:pk>/", views.updateInteractivePlatform , name="updateInteractivePlatform"),
    # path("updateInteractivePlatform/<int:platform>/", views.updateInteractivePlatform , name="updateInteractivePlatform"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)