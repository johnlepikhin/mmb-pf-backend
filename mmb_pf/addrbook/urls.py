from django.urls import re_path

from . import views

app_name = "addrbook"  # pylint: disable = invalid-name

urlpatterns = [
    re_path(r"^list/$", views.addrbook_list, name="addrbook_addrbook_list"),
    re_path(r"^info/$", views.addrbook_info, name="addrbook_addrbook_info"),
]
