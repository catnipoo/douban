from django.db import models

# Create your models here.
class MoviesInfo(models.Model):
    title = models.CharField(max_length=300,verbose_name='电影名')
    director = models.CharField(max_length=200,verbose_name='导演')
    screenwriter = models.CharField(max_length=400,verbose_name='编剧')
    starring = models.CharField(max_length=600,verbose_name='主演')
    types = models.CharField(max_length=120,verbose_name='类型')
    area = models.CharField(max_length=20,verbose_name='地区')
    language = models.CharField(max_length=20,verbose_name='语言')
    date = models.CharField(max_length=100,verbose_name='上映日期')
    lengh = models.CharField(max_length=100,verbose_name='片长')
    aka = models.CharField(max_length=500,verbose_name="又名")
    imdb_href = models.CharField(max_length=200,verbose_name='IMDb链接')
    img_url = models.CharField(max_length=300,verbose_name='图片')
    score = models.DecimalField(max_digits=3,decimal_places=1,verbose_name='评分')
    synopsis = models.TextField(verbose_name="剧情简介")

    class Meta:
        db_table = 'tb_douban'
        verbose_name = '豆瓣'
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.title