from django.conf.urls import patterns, include, url


urlpatterns = patterns('champions.views',     

    url(r'^(?P<msisdn>\d+)/activate/$', 
        'activate',
        name='champion-activate'
    ),

)
