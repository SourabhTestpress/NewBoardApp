from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
	    return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Board,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return '/board/{}/'.format(self.slug)



class Topic(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    slug = models.SlugField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    subject = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.subject)
        super(Topic,self).save(*args,**kwargs)


class Post(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE,related_name = 'posts')
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'posts')
    updated_by = models.ForeignKey(User,on_delete = models.CASCADE,null = True,related_name = '+')
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(null = True)

    def __str__(self):
        return str(self.message)[:20]