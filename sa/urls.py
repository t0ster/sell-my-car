from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from sa.apps.core.models import Car
from sa.apps.core.views import CarDetailView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.haml"), name='home'),
    url(r'^car/(?P<pk>\d+)/$', CarDetailView.as_view(template_name="index.haml"), name='car'),
    # url(r'^sa/', include('sa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
