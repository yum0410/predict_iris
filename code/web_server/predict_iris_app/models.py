from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Iris(models.Model):
    #ガクの長さ
    sepal_length = models.FloatField(default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    #ガクの幅
    sepal_width = models.FloatField(default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    #花弁の長さ
    petal_length = models.FloatField(default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    #花弁の幅
    petal_width = models.FloatField(default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])

