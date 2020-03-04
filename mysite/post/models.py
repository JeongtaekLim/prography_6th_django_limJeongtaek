# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('account.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

