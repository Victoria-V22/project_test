from django.db import models

# Create your models here.

class Bb(models.Model):
  title = models.CharField(max_length=60)
  content = models.TextField(null=True, blank=True)
  price = models.FloatField(null=True, blank=True)
  published = models.DateTimeField(auto_now_add=True, db_index=True)

class Rubric(models.Model):
  name = models.CharField(max_length=20, db_index=True,   verbose_name='Название')
  
  class Meta:
    verbose_name_plural = 'Рубрики'
    verbose_name = 'Рубрика'
    ordering = ['name']
