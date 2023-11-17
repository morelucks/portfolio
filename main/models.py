from django.db import models


    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption