from django.conf.urls import include, url
from django.contrib import admin

from .views import here, math
from restaurants.views import menu


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
    url(r'^menu/$', menu),
]
