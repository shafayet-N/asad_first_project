from django.urls import path
from . import views

app_name = 'writers'

urlpatterns = [
    path("profile/", views.view_profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="profile_edit"),
]
