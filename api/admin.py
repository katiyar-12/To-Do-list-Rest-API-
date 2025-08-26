from django.contrib import admin
from api.models import Person , Task , Date

# Register your models here.
class DateTabulurInline(admin.TabularInline) :
    model = Date
    extra = 1 

class TaskTabularInline(admin.TabularInline) :
    model = Task 
    extra = 2

class DateModelAdmin(admin.ModelAdmin) :
    fields = ['date']
    inlines = [TaskTabularInline]


class PersonModelAdmin(admin.ModelAdmin) :
    fields = ['name' , 'email']
    inlines = [DateTabulurInline]


admin.site.register(Person , PersonModelAdmin)
admin.site.register(Date , DateModelAdmin)
admin.site.register(Task)