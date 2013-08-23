from django.conf.urls import patterns, include, url


urlpatterns = patterns('faqs.views',     
    url(r'^$', 'faq_list', name='faqs-list'),
)
