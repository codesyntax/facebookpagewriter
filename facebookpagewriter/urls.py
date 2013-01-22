from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'', 'facebookpagewriter.views.fblogin', name='fblogin'),
                       )                      
