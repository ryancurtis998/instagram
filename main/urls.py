from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views


urlpatterns = [
    # url(r'^$', views.insta_index),
    url(r'^home/$',views.home_index, name="homePage"),
    url(r'^$', views.signup),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'comments/',views.save_comment, name='comment'),
    url(r'profile/',views.profile_index, name='profile'),
    url(r'update/',views.edit, name='edit'),
    url(r'^follow_or_not/(?P<user_id>\d+)$', views.togglefollow, name='follow_or_not'),
    url(r'^unlike/(?P<post_id>\d+)$', views.unlike, name='unlike'),
    url(r'^like/(?P<post_id>\d+)$', views.like, name='like')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)