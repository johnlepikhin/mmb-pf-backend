from django.urls import re_path

from . import views

app_name = "administration" # pylint: disable = invalid-name

urlpatterns = [
    re_path(r"^change_self_password/$", views.change_self_password, name="administrataion_change_self_password"),
    re_path(r"^database_operations/$", views.database_operations, name="administrataion_database_operations"),
]
