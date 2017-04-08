# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class EC2(models.Model):
    name = models.CharField(max_length=200)
    stats = models.TextField(blank=False)

    def __str__(self):
        return self.stats

# Create your models here.
