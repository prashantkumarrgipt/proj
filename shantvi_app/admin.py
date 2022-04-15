from django.contrib import admin
from .models import Category ,Post

# for configuration of category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','add_date')
    search_fields=('title',)

# for configuration of Post admin

class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=20

    class Media:
        js=('js/script.js',)

# Register your models here.

admin.site.register(Category ,CategoryAdmin)
admin.site.register(Post ,PostAdmin)
