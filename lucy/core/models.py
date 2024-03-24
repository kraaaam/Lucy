import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class BaseModel(models.Model):
    slug = models.CharField(
        default=uuid.uuid4,
        max_length=40,
        editable=False,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.slug)


class User(BaseModel, AbstractUser):
    objects = UserManager()


class TelegramChannel(BaseModel):
    slug = models.CharField(
        default=uuid.uuid4, max_length=40, editable=False, db_index=True
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class TelegramSubscriber(BaseModel):
    chat_id = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
