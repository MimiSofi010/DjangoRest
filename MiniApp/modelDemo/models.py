from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.firstName + " " +self.lastName