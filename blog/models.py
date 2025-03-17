from django.db import models
from django.utils.text import slugify


# Category
class Category(models.Model):
    name = models.CharField(max_length=100, default="exmaple")

    def __str__(self):
        return super().__str__()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    category_id = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return super().__str__()

# create contact here
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()
