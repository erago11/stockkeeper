from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Stock(models.Model):
    code = models.IntegerField('銘柄コード',validators=[MinValueValidator(1000),MaxValueValidator(9999)])
    name = models.CharField('会社名',max_length = 150)
    price = models.FloatField('登録時株価')
    now_price=models.FloatField('現在値',default=0,blank=True)
    remarks = models.TextField('備考',blank=True)
    date = models.DateTimeField('日付',default=timezone.now)
