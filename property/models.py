
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True , blank=True)



    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)    
       super(Property, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})


