from django.contrib import admin
from django.urls import include, path

urlpatterns = [path("admin/", admin.site.urls), path("posts/", include("posts.urls")), path("", include("main.urls"))]
