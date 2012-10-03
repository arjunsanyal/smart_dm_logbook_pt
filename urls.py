from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^pyHealthVault/', include('pyHealthVault.foo.urls')),

    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
    (r'^$', 'webapp.views.index'),

    (r'^mvaultaction/$', 'webapp.views.mvaultaction'),

    (r'^mvaultentry/$', 'webapp.views.mvaultentry'),

)
