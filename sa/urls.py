from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView

from sa.apps.core.models import Car
from sa.apps.core.views import CarDetailView, CarCreateView, CarDeleteView, CarUpdateView, CarPostView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListView.as_view(template_name="index.haml", model=Car, context_object_name='car_list'), name='home'),
    url(r'^car/(?P<pk>\d+)/$', CarDetailView.as_view(template_name="car.haml"), name='car'),
    url(r'^add_car/$', CarCreateView.as_view(), name='add_car'),
    url(r'^edit_car/(?P<pk>\d+)/$', CarUpdateView.as_view(), name='edit_car'),
    url(r'^delete_car/(?P<pk>\d+)/$', CarDeleteView.as_view(), name='delete_car'),
    url(r'^post_car/(?P<pk>\d+)/$', CarPostView.as_view(), name='post_car'),
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
