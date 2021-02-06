from django.contrib import admin
from movieapp.models import MovieInfo

# Register your models here.
from .models import Question

admin.site.register(Question)
# Register your models here.

class MovieDetails(admin.ModelAdmin):
    list_display=['Movie','Release_Year','Actor']
admin.site.register(MovieInfo,MovieDetails)
