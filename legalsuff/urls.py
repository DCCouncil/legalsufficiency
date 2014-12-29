from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legalsuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^suff/', 'app.views.new_legal_sufficiency', name='new_legal_sufficiency'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
