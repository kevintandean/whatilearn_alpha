from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whatilearn_alpha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #registration URL
    (r'^accounts/', include('registration.backends.default.urls')), #added login and reset password to defaults
    url(r'^accounts/profile/$', 'register.views.edit_profile', name = "edit_profile"),
    url(r'^home/$', 'register.views.home', name = "home"),
    url(r'^$', "register.views.landing", name = "landing"),
    url(r'^profile/(?P<username>\w+)/$', 'register.views.view_profile', name='view_profile'),
    url(r'^accounts/profile/edit/$', 'register.views.update_profile', name='update_profile'),
    url(r'^post/(?P<post_id>\w+)/$', 'register.views.view_post', name='view_post'),

)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)