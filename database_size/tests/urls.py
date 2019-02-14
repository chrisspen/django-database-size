
try:
    # Removed in Django 1.6
    from django.conf.urls.defaults import url, include
except ImportError:
    from django.conf.urls import url, include

try:
    # Relocated in Django 1.6
    from django.conf.urls.defaults import patterns
except ImportError:
    # Completely removed in Django 1.10
    try:
        from django.conf.urls import patterns
    except ImportError:
        patterns = None

from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

admin.autodiscover()

try:
    _patterns = [
        url(r'^admin/', include(admin.site.urls)),
    ]
except ImproperlyConfigured:
    _patterns = [
        url(r'^admin/', admin.site.urls),
    ]

if patterns is None:
    urlpatterns = _patterns
else:
    urlpatterns = patterns('', *_patterns)
