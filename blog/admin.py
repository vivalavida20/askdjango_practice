from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	# list_display할 수 있는 요소는 필드명/속성명/함수명(인자없는)
	list_display = ['id', 'title', 'content_length','created_at', 'updated_at']


	def content_length(self, post):
		return mark_safe("<strong>{}글자</strong>".format(len(post.content)))

	# admin에 노출하고 싶은 컬럼명
	content_length.short_description = '글자수'

#admin.site.register(Post, PostAdmin)
