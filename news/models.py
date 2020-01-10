from django.db import models

from django.conf import settings

from datetime import datetime
from django.utils import timezone



class Article(models.Model):
	title = models.CharField(max_length=200, default="")
	href = models.CharField(max_length=200, default="")
	publisher = models.CharField(max_length=100, default="")
	introduction = models.TextField(default="")
	date_scraped = models.DateTimeField(default=timezone.now)
	date_published = models.DateTimeField(default=timezone.now)