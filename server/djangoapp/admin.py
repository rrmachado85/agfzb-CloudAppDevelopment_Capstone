from django.contrib import admin
# from .models import related models
from djangoapp.models import CarMake
from djangoapp.models import CarModel


# Register your models here.

# CarModelInline class
class CarModelInline (admin.StackedInline):
    model = CarModel
    extra = 5

class CarModelAdmin(admin.ModelAdmin):
    fields = ['Type', 'Dealear_id', 'Name', 'Description']
# CarModelAdmin class
admin.site.register(CarModel)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['Name', 'Description']
    inlines = [CarModelInline]
admin.site.register(CarMake)