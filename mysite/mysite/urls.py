from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from .views import here, math, welcome
from restaurants.views import menu, list_restaurants


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
    url(r'^menu/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
]
