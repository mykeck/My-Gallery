from django.contrib import admin
from .models import Location,Categories,Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('Categories',)

admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Image,ImageAdmin)    
