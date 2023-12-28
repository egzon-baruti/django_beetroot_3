from django.db import models

class Post(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.text[:50] + "..."

    
    