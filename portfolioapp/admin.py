from django.contrib import admin

# Register your models here.
from portfolioapp.models import Portfolio, Photo, Category, Like, Comment

admin.site.register(Portfolio)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)