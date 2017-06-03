from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse

class PostListView1(View):
    def get(self, request):
        name = '공유2'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>AskDjango</h1>
            <p>{name}</p>
            <p>템플릿 테스트</p>
        '''

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()

# 직접 해볼 것
class PostListView3(View):

    def get_json_response(self):
        return JsonResponse({
            'message' : '안녕 파이썬 장고',
            'items' : ['파이썬', '안녕', '장고']
        }, json_dumps_params={'ensure_ascii' : False })

class PostListView3(View):
    pass