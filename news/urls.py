from django.urls import path

from news.apps import NewsConfig
from news.views import NewsListAPIView, NewsUpdateAPIView, NewsRetrieveAPIView

app_name = NewsConfig.name

urlpatterns = [
    path('list/', NewsListAPIView.as_view(), name='news_list'),
    path('list/<int:pk>', NewsRetrieveAPIView.as_view(), name='news_detail'),
    path('edit/<int:pk>/', NewsUpdateAPIView.as_view(), name='news_update'),
]
