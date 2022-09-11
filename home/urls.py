from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage, name="home"),
    path("request_list",views.request_list, name="request_list"),
    path("delete-request/<int:id>",views.delete_request, name = "delete_request"),
    path("request",views.request,name="request"),
    path("logout",views.logoutuser,name="logout")
] 