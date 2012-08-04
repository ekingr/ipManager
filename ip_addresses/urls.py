from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('ip_addresses.views',
    (r'^networkaddress/$', 'display'),
    (r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/$',
        'display'),
)
