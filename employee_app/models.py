from django.db import models


# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
