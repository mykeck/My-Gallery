from django.db import models
from django.db.models import Q

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()            

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete        
        
    
class Image(models.Model):
    title = models.CharField(max_length=60)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(Q(categories__category=search_term) | Q(title__icontains=search_term) | Q(location__location=search_term))

        return images  

    @classmethod
    def filter_by_location(cls,location_id):
        images = cls.objects.filter(id = location_id)

        return images

