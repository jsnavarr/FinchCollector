from django.contrib import admin
from .models import User, Phone, Meal

# Register your models here.
admin.site.register(User)
admin.site.register(Phone)
admin.site.register(Meal)
