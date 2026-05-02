from django.db import models
from django.db.models import CASCADE
from users.models import User
from posts.models import Post

class Comment(models.Model):
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete= CASCADE,null=True)
    # por que cuando se elmina un post se elimine el comentario
    posts=models.ForeignKey(Post,on_delete=CASCADE,null=True)
