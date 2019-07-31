from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .fields import ThumbnailImageField



# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goodmenu:album_detail', args=(self.id,))

class GoodStar(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    img = ThumbnailImageField(upload_to='goodstar',null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Goodmenu(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    goodstar = models.ForeignKey('GoodStar',on_delete=models.CASCADE, related_name='goodstar',null=True)
    area = models.CharField(max_length=30,default='강동')
    title = models.CharField(max_length=50)
    smallbody = models.CharField(max_length=500,null=True)
    body = models.TextField(null=True)
    smallimg = ThumbnailImageField(upload_to='goodmenu/%Y/%m')
    detailimg = ThumbnailImageField(upload_to='goodmenu/%Y/%m')
    location = ThumbnailImageField(upload_to='goodmenu/%Y/%m')
    url = models.URLField('url',null=True)
    date = models.DateTimeField(auto_now_add=True)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    mapleft = models.FloatField(null=True)
    mapright = models.FloatField(null=True)

    like = models.ManyToManyField(User, related_name='goodmenulike_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='goodmenufavorite_post', blank=True)

    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('goodmenu:goodmenu_detail', args=(self.id,))

    @property
    def update_counter(self):
        self.hit = self.hit +1
        self.save()


