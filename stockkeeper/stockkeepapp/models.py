from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Stock(models.Model):
    code = models.IntegerField('銘柄コード',validators=[MinValueValidator(1000),MaxValueValidator(9999)])
    price = models.FloatField('登録時株価')
    memo = models.TextField('備考')
