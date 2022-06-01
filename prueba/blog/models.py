from django.db import models
from django.urls import reverse

# Create your models here.

class Post (models.Model):
    #text = models.TextField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            'auth.User',
            on_delete = models.CASCADE,
    )
    body = models.TextField()
    
    def str(self):
        return self.title + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        #return reverse('post_detail', args=(str(self.id )))
        return reverse('home')
