from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^download/$', views.excel_download),

    url(r'^cbv/list1/$', views.post_list1),
    url(r'^cbv/list2/$', views.post_list2),
    url(r'^cbv/list3/$', views.post_list3),
    url(r'^cbv/download/$', views.excel_download),
]