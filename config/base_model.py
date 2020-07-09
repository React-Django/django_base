from django.db import models

from .case.mixins import FromCamelCase, ToCamelCase


class BaseClass(models.Model, FromCamelCase, ToCamelCase):
    active = models.BooleanField(default='True')
    created_at = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=255, default='')
    updated_at = models.DateField(auto_now=True)
    updated_by = models.CharField(max_length=255, default='')

    class Meta:
        abstract = True
