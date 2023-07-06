from django.contrib import admin
from.models import ToDoList
class TodoLIstAdmin(admin.ModelAdmin):
    todolist = ("user","title","description","complete","create")
admin.site.register(ToDoList)    
# Register your models here.
