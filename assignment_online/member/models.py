from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=9)

    class Meta:
        unique_together = (("user","code"))
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + self.code

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name