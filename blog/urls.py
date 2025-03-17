from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/detail/<str:slug>", views.detail, name="detail"),
    path("new_url_mmbu", views.newUrl, name="newUrlTest"),
    path("old_url", views.oldUrl, name="oldUrl"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_page, name="about"),
]
