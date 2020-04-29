from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.SerchView.as_view(), name='serch'),
    url(r'^searchdetail/$',views.LianxiangView.as_view()),
    url(r'^searchlist/(?P<page_num>\d+)/$',views.ListView.as_view()),
    url(r'^detail/(?P<movie_id>\d+)/$', views.DetailView.as_view()),
    ]