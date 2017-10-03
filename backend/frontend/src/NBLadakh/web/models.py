from django.db import models

# Create your models here.
class Image(models.Model):
    code = models.CharField(max_length=50)
    low_res_url = models.URLField()
    embed_code = models.TextField()
