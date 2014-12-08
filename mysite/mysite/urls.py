from django.conf.urls import include, url
from django.contrib import admin

from .views import here


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
]
