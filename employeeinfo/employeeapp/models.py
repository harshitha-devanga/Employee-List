from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=200)
    esalary=models.IntegerField()
    erole=models.CharField(max_length=200)

    def __str__(self) :
        return self.ename

