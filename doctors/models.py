from django.db import models


class Doctor(models.Model):
    name = models.CharField('Nome', max_length=100)
    age = models.IntegerField('Idade')
    crm = models.IntegerField('CRM')



