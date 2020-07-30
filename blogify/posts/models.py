from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # author = 
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # auto set time when post is created
    image = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title

    def post_snippet(self):
        return self.body[:100] + "..." # show a snippet of the post