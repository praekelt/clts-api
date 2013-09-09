from django.conf.urls import patterns, include, url


urlpatterns = patterns('pages.views',     
    url(r'(?P<category_slug>\w+)/$', 'pages_list', name='pages-list'),

    # ^(?P<msisdn>\d+)
)
