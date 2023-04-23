from django.urls import path
from . import views

urlpatterns = [
    path("",views.TodoApiListView,name='listtodo')
]