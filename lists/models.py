from django.db import models

# Create your models here.

class List(models.Model):
    ''' элемент  списка '''
    pass

class Item(models.Model):
    ''' элемент списка '''
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
    #on_delete=models.CASCADE) добавлено мною


