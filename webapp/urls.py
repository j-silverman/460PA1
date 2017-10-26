from django.conf.urls import url
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^logged_out/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logged_out'),
    url(r'^profile/$', views.profile, name='profile'),
    ]
