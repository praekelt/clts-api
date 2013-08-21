from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from rest_framework import routers

from champions.views import ChampionViewSet


router = routers.DefaultRouter()
router.register(r'champions', ChampionViewSet)

admin.autodiscover()

urlpatterns = patterns('',	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/v1/', include(router.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^public/media/(?P<path>.*)$',
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

