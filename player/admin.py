from django.contrib import admin

# Register your models here.
from player.models import Song, Statistic


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    pass
