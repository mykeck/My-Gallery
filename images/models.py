from django.db import models

# Create your models here.
class image(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    post_date = models.DateTimeField(auto_now_add=True)
