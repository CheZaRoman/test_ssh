from django.conf.urls import url
from django.urls import path

from player.views import AuthorApiView

urlpatterns = [
    url(r'author/', AuthorApiView.as_view())
]