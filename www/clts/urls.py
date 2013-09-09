from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/v1/champions/', include('champions.urls')),
    url(r'^api/v1/faqs/', include('faqs.urls')),
    url(r'^api/v1/pages/', include('pages.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^public/media/(?P<path>.*)$',
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

