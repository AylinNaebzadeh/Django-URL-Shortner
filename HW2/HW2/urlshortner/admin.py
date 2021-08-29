from django.contrib import admin
from .models import Url

# Register your models here.




class URLAdmin(admin.ModelAdmin):
    list_display = ('url_id' , 'link')

admin.site.register(Url,URLAdmin)
