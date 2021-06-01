from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Portfolio


@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(photographer=instance)
        print("Profile created")


#post_save.connect(create_portfolio, sender=User)


@receiver(post_save, sender=User)
def update_portfolio(sender, instance, created, **kwargs):
    if not created:
        instance.portfolio.save()
        print("Profile updated")


#post_save.connect(update_portfolio, sender=User)
