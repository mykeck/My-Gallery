from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
        
    
class image(models.Model):
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
        images = cls.objects.filter(Q(categories_category = search_term) | Q)        
