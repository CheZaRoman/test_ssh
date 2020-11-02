from django.conf.urls import url
from player.views import AuthorApiView, StatisticView

urlpatterns = [
    url(r'author/', AuthorApiView.as_view()),
    url(r'statistic/', StatisticView.as_view())
]