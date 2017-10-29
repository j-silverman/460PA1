from django.conf.urls import url
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^logged_out/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logged_out'),
    #url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/upload$', views.model_form_upload, name = 'upload'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.profile, name='profile'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name= 'change_friends'),
    url(r'album/$', views.album_upload, name = 'album_up'),
    url(r'^album/(?P<username>[a-zA-Z0-9]+)$', views.album_list, name = 'album_list'),
    url(r'^picture/(?P<document>[a-zA-Z0-9]+)$', views.picture, name = 'picture'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'search$', views.search, name = 'search'),
    url(r'name_search$', views.name_search, name = 'name_search')
    ] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
