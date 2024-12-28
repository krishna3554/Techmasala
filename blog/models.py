from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=13)
    Img = models.ImageField(upload_to='images/', default="")
    timeStamp = models.DateField(blank=True)

    
    def __str__(self):
        return 'message from ' + self.title + ' : eamil - '+self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13]+"..."+ "by" + self.user.username
    
