from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100,verbose_name='имя')
    age = models.IntegerField(verbose_name="")
    city = models.CharField(max_length=100,verbose_name="город")
    email = models.EmailField()
    created_at  = models.DateTimeField(auto_now_add=True)


class Meta:
    verbose_name = "Students"
    verbose_name_plural = "Students"
