from django.urls import path

from .views import IndexView, WorkView, AboutView, ContactView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("work/", WorkView.as_view(), name="work"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
]
