from django.db import models
from django.db.models import Model, CharField, EmailField, DateTimeField


class ProjectRequest(Model):
    name = CharField(max_length=255,verbose_name='Имя заказчика')
    email = EmailField(null=True, blank=True,verbose_name="Email")
    phone = CharField(max_length=17,null=True, blank=True,verbose_name="Телефон")
    created_at = DateTimeField(null=True,blank=True,verbose_name='Время поступления')