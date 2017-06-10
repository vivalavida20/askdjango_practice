from django.http import Http404
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
        
    return render(request, 'blog/post_list.html', {
        'post_list':qs
    })

def post_detail(request, id):
	
	# 아래 get_object_or_404로 예외처리하는 것이 가장 간단하다.
	# try:
	# 	post = Post.objects.get(id=id)
	# except Post.DoesNotExist:
	# 	raise Http404

	post = get_obect_or_404(Post, id=id)

	return render(request, 'blog/post_detail.html', {
		'post' : post,
	})