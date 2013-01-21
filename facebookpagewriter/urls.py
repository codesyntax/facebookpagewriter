from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'niagarank.views.fblogin', name='nrgk_fblogin'),
                       )                      
