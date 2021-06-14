from . import views
from .import blogview
from .import scrapper
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("service", views.service, name="service"),
    #tools
    path("costcalculator", views.costcal, name="costcal"),
    #news
    path("news/", blogview.NewsView.as_view(), name="news"),
    path("news/<slug:slug>",blogview.NewsDetail.as_view(),name="detail"),
    #livenepse
    path('livenepse/',scrapper.main, name='livenepse'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

