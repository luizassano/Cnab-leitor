from django.contrib import admin
from django.urls import include, path
from transactions import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("uploadfile/", views.upload, name="upload"),
    path("", include("transactions.urls")),
]