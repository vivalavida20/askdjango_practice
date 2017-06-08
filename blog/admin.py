from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
#unregister도 가능하다.
admin.site.unregister(Post)
admin.site.register(Post)
