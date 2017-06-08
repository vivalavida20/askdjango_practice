from django.contrib import admin
from .models import Post
# Register your models here.

#커스터마이징
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'created_at', 'updated_at']

admin.site.register(Post, PostAdmin)
