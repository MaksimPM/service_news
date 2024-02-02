from django.contrib import admin

from news.models import News, NewsCategories

admin.site.register(News)
admin.site.register(NewsCategories)
