
from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('database_size.tests.views',
    (r'^admin/', include(admin.site.urls)),
)
