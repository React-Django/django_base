from django.db import models

from config.base_model import BaseClass


class TestModel(BaseClass):

    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
