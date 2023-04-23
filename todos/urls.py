from django.urls import path
from . import views

urlpatterns = [
    path("",views.TodoApiListView.as_view(),name='listtodo'),
    path("<int:pk>/", views.TodoApiDetailView.as_view(),name='detailtodo')
]