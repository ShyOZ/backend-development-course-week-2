from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("<str:name>/", views.display_message, name="display-message"),
]
