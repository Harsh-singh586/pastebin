# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class data(models.Model):
    key = models.CharField(max_length=4)
    text = models.CharField(max_length=10000)
    def __str__(self):
        return self.key





# Create your models here.
