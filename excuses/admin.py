from django.contrib import admin

# Register your models here.
from .models import RootCause, ActionPlan, Bug

admin.site.register(RootCause)
admin.site.register(ActionPlan)
admin.site.register(Bug)