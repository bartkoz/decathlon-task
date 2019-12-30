from django.dispatch import receiver
from api.models import Comment
from django.db.models.signals import post_save, post_delete
from django.db.models import F


@receiver(post_save, sender=Comment)
def increment_comments_count(sender, instance, **kwargs):
    """
    Adds +1 to movie when commented
    """
    instance.movie.comments_count = F('comments_count') + 1
    instance.movie.save()


@receiver(post_delete, sender=Comment)
def decrement_comments_count(sender, instance, **kwargs):
    """
    Substracts 1 when comment deleted
    """
    instance.movie.comments_count = F('comments_count') - 1
    instance.movie.save()
