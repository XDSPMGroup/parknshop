from django.conf.urls import patterns, include, url
from django.contrib import admin
#from account.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anybuy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    #url(r'^account/$', views.register, name='register'),
    #url(r'^account/register/$',views.register, name = 'register'),
)
