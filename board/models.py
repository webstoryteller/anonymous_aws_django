from django.db import models
# Create your models here.
from user.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(null=True)

    class Meta:
        db_table = "post"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content= models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"