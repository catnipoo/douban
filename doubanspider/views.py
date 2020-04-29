import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from doubanspider.models import MoviesInfo


class SerchView(View):
    def get(self,request):
        return render(request,'serch.html')

class LianxiangView(View):
    def get(self,request):
        q = request.GET.get('q')
        recontents = MoviesInfo.objects.filter(title__contains=q)
        rejson = []
        for recontent in recontents:
            rejson.append(recontent.title)
        return HttpResponse(json.dumps(rejson), content_type='application/json')
class ListView(View):
    def post(self,request,page_num):

        q = request.POST.get('q')
        recontents = MoviesInfo.objects.filter(Q(title__contains=q)|Q(starring__contains=q)|Q(types__contains=q))
        from django.core.paginator import Paginator
        paginator = Paginator(recontents, 5)
        page_movies = paginator.page(page_num)
        total_pages = paginator.num_pages
        context = {
            'page_movies': page_movies,  # 分页后数据
            'total_page': total_pages,  # 总页数
            'page_num': page_num,  # 当前页码
        }
        return render(request,'list.html',context)

class DetailView(View):
    def get(self,request,movie_id):
        try:
            mov = MoviesInfo.objects.get(id=movie_id)
        except Exception:
            return render(request,'404.html')
        context = {
            'mov':mov
        }
        return render(request,'detail.html',context)