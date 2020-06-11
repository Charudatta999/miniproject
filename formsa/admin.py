from django.contrib import admin
# Register your models here.
from .models import Entry,Profile


# class regiAdmin(admin.ModelAdmin):
#     fieldsets = [('Name',{"fields": ['name','password']}),
#                  ('Roll',{'fields': ['prn','div']})]


admin.site.register(Entry)
admin.site.register(Profile)
