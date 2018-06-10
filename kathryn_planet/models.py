# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    body = models.CharField(max_length=2054, blank=False, null=False)
