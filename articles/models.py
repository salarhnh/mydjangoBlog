from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    #picture
    #author

    def __str__(self):
        return self.title


    def snippet(self):
        return self.body[:50] + '...'
