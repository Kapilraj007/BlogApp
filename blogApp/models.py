from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True , related_name='category')
    blog_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    blog_description = models.TextField()
    post_date = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return self.blog_title + "==>" + str(self.author)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title + "-" + str(self.post_date))
        return super().save(*args, **kwargs)
    
class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.blog
    