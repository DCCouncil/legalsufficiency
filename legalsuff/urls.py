from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'legalsuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^view/$', 'app.views.view_sufficiencies', name='view_sufficiencies'),
    url(r'^view/(?P<pk>[\w|-]+)/$', 'app.views.print_sufficiencies', name='print_sufficiencies'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^suff/$', 'app.views.new_legal_sufficiency', name='new_legal_sufficiency'),
    url(r'^suff/(?P<pk>[\w|-]+)/$', login_required(views.LegalSufficiencyUpdate.as_view()), name='suff-detail'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'redirect_field_name':'/'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url(r'^redactor/', include('redactor.urls')), 
)
