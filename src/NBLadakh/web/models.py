from django.db import models

# Create your models here.
class Image(models.Model):
    code = models.CharField(max_length=50)
    low_res_url = models.URLField()
    embed_code = models.TextField()

    @classmethod
    def create(cls, code, low_res_url, embed_code):
        img = cls(code=code, low_res_url=low_res_url, embed_code=embed_code)
        return img

#class ImageManager(models.Manager):
 #   def create_Image(self, code, low_res_url, embed_code):
  #      img = self.create(code=code, low_res_url=low_res_url,
        #        embed_code=embed_code)
       # return img
