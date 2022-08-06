from importlib.metadata import requires
from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import Profile

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title



class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, default='default.png', upload_to='profiles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return '%s - %s' % (self.article.title, self.owner)

    class Meta:
        ordering = ['-created']