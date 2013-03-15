from django.conf.urls import patterns, include, url

from realestate.core.api import auth, user, adv, vcard


urlpatterns = patterns('',

    # Authentication URLs.
    url(r'^register/?$', auth.register),
    url(r'^login/?$', auth.login_view),
    url(r'^logout/?$', auth.logout_view),

    # User resource URLs.
    url(r'^user/?$', user.UserResource.as_view()),
    url(r'^user/(?P<username>[^/]+)/?$', user.UserResource.as_view()),

    # Adv resource URLs.
    url(r'^adv/?$', adv.AdvResource.as_view()),
    url(r'^adv/(?P<adv_id>[^/]+)/?$', adv.AdvResource.as_view()),

    # Virtual Card resource
    url(r'^vcard/?$', vcard.VCardResource.as_view()),
    url(r'^vcard/(?P<vcard_id>[^/]+)/?$', vcard.VCardResource.as_view()),
)