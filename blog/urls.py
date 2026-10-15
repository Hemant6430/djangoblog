from django.urls import path
from .views import (
    home,
    about,
    base,
    contact,
    post_detail,
    post_create,
    post_edit,
    post_delete,
    RegisterView,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("base/", base, name="base"),
    path("contact/", contact, name="contact"),

    path("post/create/", post_create, name="post_create"),
    path("post/<slug:slug>/", post_detail, name="post_detail"),

    path("post/<int:pk>/edit/", post_edit, name="post_edit"),
    path("post/<int:pk>/delete/", post_delete, name="post_delete"),

    path("register/", RegisterView.as_view(), name="register"),
]