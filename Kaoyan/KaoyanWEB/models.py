from django.db import models

# Create your models here.

#商品的分类
#模型类

class GoodsCategory(models.Model):
    cag_name = models.CharField(max_length=30)
    cag_css = models.CharField(max_length=20)
