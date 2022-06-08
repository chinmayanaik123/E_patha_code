from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    Place_name = models.CharField(max_length=50)
    place = models.CharField(max_length=500, default="")
    About = models.CharField(max_length=5000, default="")
    headding = models.CharField(max_length=500, default="")
    info = models.CharField(max_length=5000, default="")
    headdings = models.CharField(max_length=500, default="")
    informations = models.CharField(max_length=5000, default="")
    info_date = models.DateField()
    Images = models.ImageField(upload_to='e_patha/images', default="")

    def __str__(self):
        return self.Place_name 

