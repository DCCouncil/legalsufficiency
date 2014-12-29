from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legalsuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^suff/$', 'app.views.new_legal_sufficiency', name='new_legal_sufficiency'),
    url(r'^suff/(?P<pk>[\w|-]+)/$', views.LegalSufficiencyUpdate.as_view(), name='suff-detail'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^redactor/', include('redactor.urls')), 
)
