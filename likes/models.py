from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # type (product, video, Category)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID
    object_id = models.PositiveIntegerField()
    # get objet that liked with query
    content_object = GenericForeignKey()