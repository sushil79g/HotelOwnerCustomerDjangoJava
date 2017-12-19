from django.conf.urls import url,include
from django.contrib.auth.models import User
from . import views
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import login,logout
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    
    # url(r'^register', views.register, name='register'),
    url('^/owner/',include('owner.api.urls')),
    url(r'^signup/$', views.User, name='register'),

    url(r'^login/',views.login, name= 'login'),
    url(r'^after',views.after,name='after'),
    url(r'^order',views.order,name='order'),
    url(r'^status',views.status,name='status'),
    url(r'^menu',views.menu,name='menu'),
    url(r'^update/(?P<person_id>[0-9]+)$',views.updatePending, name='updatePending')


# url(r'^login/$', login, {'template_name': 'signup.html'}, name='login'),
# url(r'^login/$', login, {'template_name': 'signup.html'}, name='logout'),
    # url(r'^login',views.login,name='login'),
    # url(r'^register/done', views.registerdone, name='register'),


]