from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Position)
admin.site.register(Employee)
# Register your models here.
#admin.site.register(model.Position)
#admin.site.register(Employee)