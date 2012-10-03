from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^pyHealthVault/', include('pyHealthVault.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
    (r'^$', 'smart_hv_django.webapp.views.index'),

    (r'^mvaultaction/$', 'smart_hv_django.webapp.views.mvaultaction'),

    (r'^mvaultentry/$', 'smart_hv_django.webapp.views.mvaultentry'),

)
