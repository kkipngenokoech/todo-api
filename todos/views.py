from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
class TodoApiListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoApiDetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer