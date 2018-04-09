from django.conf.urls import url
from django.contrib import admin
from . import views 
app_name='app'
urlpatterns = [
    url(r'home/$',views.home,name='home'),
    url(r'home/(?P<code>.*)/$',views.home,name='home'),
    
    url(r'buy/$',views.buy,name='buy'),
    url(r'buy/(?P<code>.*)/$',views.buy,name='buy'),
    
    url(r'sell/$',views.sell,name='sell'),
    url(r'sell/(?P<code>.*)/$',views.sell,name='sell'),

    url(r'register/$',views.register,name='register'),
    url(r'register/(?P<user_id>.*)/$',views.register,name='register'),

    url(r'logout/$',views.logout,name='logout'),
]