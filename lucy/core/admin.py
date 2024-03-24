from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, TelegramChannel, TelegramSubscriber

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "email")


@admin.register(TelegramChannel)
class TelegramChannelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "slug",
        "name",
        "token",
        "user",
        "is_active",
    )


@admin.register(TelegramSubscriber)
class TelegramSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "chat_id",
        "username",
        "first_name",
    )