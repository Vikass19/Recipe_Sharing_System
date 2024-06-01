from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipi(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank= True)
    recipi_name = models.CharField(max_length=200)
    recipi_description = models.TextField()
    recipi_image = models.ImageField(upload_to='media/')
    pub_date = models.DateTimeField(null=True)
    recipi_view_count = models.IntegerField(default=1)

