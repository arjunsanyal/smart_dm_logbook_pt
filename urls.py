from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^$', 'app.views.index'),
    (r'^mvaultaction/$', 'app.views.mvaultaction'),
    (r'^main/$', 'app.views.main'),
    (r'^main/css/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.BASE_DIR + '/app/css/'
    }),
    (r'^main/img/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.BASE_DIR + '/app/img/'
    }),
    (r'^main/js/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.BASE_DIR + '/app/js/'
    }),
    (r'^main/lib/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.BASE_DIR + '/app/lib/'
    }),
    (r'^main/partials/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.BASE_DIR + '/app/partials/'
    })
)
