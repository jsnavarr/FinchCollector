from django.contrib import admin
from .models import User, Phone, Meal, Photo

# Register your models here.
admin.site.register(User)
admin.site.register(Phone)
admin.site.register(Meal)
admin.site.register(Photo)
