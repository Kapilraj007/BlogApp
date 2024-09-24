from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','category','blog_title','author','post_date','is_public')
    list_display_links =('id','blog_title')
    search_fields =('blog_title',)
    list_editable = ('is_public',)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Category)

