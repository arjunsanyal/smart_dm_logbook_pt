from django.conf.urls.defaults import *
urlpatterns = patterns('',
    (r'^$', 'app.views.index'),
    (r'^mvaultaction/$', 'app.views.mvaultaction'),
    (r'^start/$', 'app.views.start')
)
