from django.conf.urls import include, url
from django.contrib import admin

from .views import here, math


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
]
