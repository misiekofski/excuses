from django.contrib import admin

# Register your models here.
from .models import RootCause, ActionPlan

admin.site.register(RootCause)
admin.site.register(ActionPlan)