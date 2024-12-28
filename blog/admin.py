from django.contrib import admin
from blog.models import Post, BlogComment


admin.site.site_header = "Techmasala"
admin.site.site_title = "Techmasala Admin Panel"
admin.site.index_title = "Welcome to Tachmasla Admin Panel "
# Register your models here.
admin.site.register(( BlogComment))
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)