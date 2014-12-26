from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView

from . import views
import restaurants.views


urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', include(admin.site.urls)),

    url('^index/$', TemplateView.as_view(template_name='index.html')),
    url(r'^accounts/register/$', views.register),
    url(r'^here/$', views.HereView.as_view()),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', views.math),
    url(r'^welcome/$', views.welcome),

    url(r'^menu/(?P<pk>\d+)/$', restaurants.views.MenuView.as_view()),
    url(r'^restaurants_list/$', restaurants.views.RestaurantsView.as_view()),
    url(r'^comment/(\d{1,5})/$', restaurants.views.comment),
]
