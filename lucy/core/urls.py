from django.urls import path

from . import views

urlpatterns = [
    path("telegram/start", views.TelegramStartView.as_view(), name="telegram-start")
]
