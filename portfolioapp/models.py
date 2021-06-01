from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField, CharField, ForeignKey, BooleanField, TextField, OneToOneField, DateTimeField
from django.urls import reverse


class Portfolio(models.Model):
    photographer = OneToOneField(User, on_delete=models.CASCADE)
    cover_image = ImageField(upload_to='images/cover_images/', default='defaults/default-cover-pic.jpg')
    profile_pic = ImageField(upload_to='images/profile_pics', default='defaults/default_profile_pic.jpg')
    location = CharField(max_length=50, blank=True, null=True, default='Planet Earth')  # country or city of origin
    artistic_name = CharField(max_length=50,default='My photography portfolio') #for photographers who present themselves with artistic names
    bio = TextField(null=True,blank=True,default='My bio') #photographer's biography

    def __str__(self):
        return self.artistic_name + ' | ' + self.photographer.__str__()

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])


class Category(models.Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('discover-photos')


class Photo(models.Model):
    light = [
        ('Natural light', 'Natural light'),
        ('Studio light', 'Studio light'),
        ('Mixed light', 'Mixed light')
    ]

    image = ImageField(upload_to='images/')
    upload_date = DateTimeField(auto_now_add=True)
    portfolio = ForeignKey(Portfolio, on_delete=models.CASCADE)
    category = CharField(max_length=50)

    title = CharField(max_length=50, blank=False, null=False)
    description = CharField(max_length=150, blank=True)

    camera_name = CharField(max_length=100, default='unknown',blank=True)
    lens = CharField(max_length=100, default='unknown',blank=True)
    used_light = CharField(max_length=50, choices=light, default='Natural light')

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.title + " | " + str(self.portfolio.photographer) + " | " + str(self.upload_date)

    def get_absolute_url(self):
        return reverse('portfolio-photo-detail', args=[str(self.id)])


class Like(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    photo = ForeignKey(Photo, on_delete=models.CASCADE)
    created_on = DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = ForeignKey(User, on_delete=models.CASCADE)
    photo = ForeignKey(Photo, on_delete=models.CASCADE)
    body = TextField()
    created_on = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']



