from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'enterChoice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^choose/$', 'choose.views.index'),
    url(r'^choose/checkChoices/$', 'choose.views.checkChoices'),
    url(r'^choose/loadRoll/$', 'choose.views.loadRoll'),
    url(r'^choose/getRoll/$', 'choose.views.getRoll'),
    url(r'^choose/refresh/$', 'choose.views.refresh'),
)
