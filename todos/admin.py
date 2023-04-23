from django.contrib import admin
from .models import Todo

# Register your models here.

# this class below when you go to view the list of created todos it will show both the title and the body instead of just the title
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')

admin.site.register(Todo, TodoAdmin)
