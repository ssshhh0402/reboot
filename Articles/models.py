from django.db import models

# Create your models here.

# Reporter(1) - Article(N)
# reporter = name


class Reporter(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    

# Article(1) - Comment(N)
# comment - content
class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE) 