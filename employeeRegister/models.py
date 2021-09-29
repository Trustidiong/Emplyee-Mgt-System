from django.db import models

# Create your models here.
#THE EMPLOYEE POSITION TABLE
class Position(models.Model):
    title = models.CharField(max_length=100)

# Returns the title from the database
    def __str__(self):
        return self.title

#THE EMPLOYEE TABLE
class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=16)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

class Salary(models.Model):
    Amount = models.CharField(max_length=9)
