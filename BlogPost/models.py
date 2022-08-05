from datetime import date, datetime
from pyexpat import model
from turtle import heading, title
from venv import create
from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.model) :
    title = models.CharField(max_length=100),
    heading = models.CharField(max_length=100),
    body = models.CharField(max_length=1000000),
    create_at = models.DateTimeField(default=datetime.now, blank=True)