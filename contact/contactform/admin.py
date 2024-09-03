from django.contrib import admin
from api.models import Contact_Enquriy
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone']

admin.site.register(Contact_Enquriy,ContactAdmin)

