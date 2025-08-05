from django.db import models
from django.contrib.sessions.models import Session
from main.models import Product, ProductSize
from decimal import Decimal


class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)


