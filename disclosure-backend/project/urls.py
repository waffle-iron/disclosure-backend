from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from rest_framework.routers import SimpleRouter

import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.homepage_view),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True,
    }),
    url(r'^docs/', include('rest_framework_swagger.urls'))
)

# Register all API Viewsets:
api = SimpleRouter()
api.register(r'contributions', views.Contribution)
urlpatterns += api.urls
