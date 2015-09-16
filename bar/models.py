from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, db_index=True)


class Car(models.Model):
    name = models.CharField(max_length=50)
