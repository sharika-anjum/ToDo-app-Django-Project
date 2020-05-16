from django.db import models


# Create your models here
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pwd = models.CharField(max_length=80)
    class Meta:
        db_table = "user"

    def __str__(self): #this function will help me to get every value that we will store inside user table
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=500)
    create = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.title
