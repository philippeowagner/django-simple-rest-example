from django.conf.urls import patterns, include, url

from realestate.core.api import auth, user, adv, object, friend, message


urlpatterns = patterns('',

    # Authentication URLs.
    url(r'^register/?$', auth.register),
    url(r'^login/?$', auth.login_view),
    url(r'^logout/?$', auth.logout_view),

    # User resource URLs.
    url(r'^user/?$', user.UserResource.as_view()),
    url(r'^user/(?P<username>[^/]+)/?$', user.UserResource.as_view()),

    # User resource URLs.
    url(r'^friend/?$', friend.FriendResource.as_view()),
    url(r'^friend/(?P<friend_id>[^/]+)/?$', friend.FriendResource.as_view()),

    # Adv resource URLs.
    url(r'^adv/?$', adv.AdvResource.as_view()),
    url(r'^adv/(?P<adv_id>[^/]+)/?$', adv.AdvResource.as_view()),

    # Virtual Card resource
    url(r'^object/?$', object.ObjectResource.as_view()),
    url(r'^object/search/?$', object.search),
    url(r'^object/(?P<object_id>[^/]+)/?$', object.ObjectResource.as_view()),

    # Messages resource URLs.
    url(r'^message/?$', message.MessageResource.as_view()),
    url(r'^message/(?P<message_id>[^/]+)?$', message.MessageResource.as_view()),

)
