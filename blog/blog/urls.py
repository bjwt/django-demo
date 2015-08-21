from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^abc/$', 'learn.views.index', name='home'),# Notice this line
    url(r'^meta/$', 'learn.views.display_meta', name='home'),# Notice this line
    url(r'^search-form/$', 'learn.views.search_form',name='home'),
    url(r'^search/$', 'learn.views.search',name='home'),
    url(r'^time/$', 'learn.views.current_datetime', name='home'),# Notice this line
    url(r'^time/plus/(\d{1,2})/$', 'learn.views.hours_ahead'),
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
