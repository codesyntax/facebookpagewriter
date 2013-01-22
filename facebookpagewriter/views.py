import hashlib
import random
import string
import urllib2
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings
from django.contrib.sites.models import get_current_site

from facebookpagewriter.models import FacebookConfig
import datetime

APP_ID = getattr(settings, 'FB_APP_ID')
APP_SECRET = getattr(settings, 'FB_APP_SECRET')

def fblogin(request):
    current_site = get_current_site(request)
    if 'code' not in request.GET:
        state = hashlib.sha224(''.join(random.sample(string.printable,40))).hexdigest()
        dialog_url = "https://www.facebook.com/dialog/oauth?client_id=%(id)s&redirect_uri=http://%(site)s%(url)s&state=%(state)s&scope=publish_actions,status_update,publish_stream,manage_pages" % {'id':APP_ID,'state': state, 'url': reverse('fblogin'),'site':current_site.domain}
        return HttpResponseRedirect(dialog_url)
    else:
        #state = request.GET['state']
        code = request.GET['code']
        access_token_url = 'https://graph.facebook.com/oauth/access_token?client_id=%(id)s&redirect_uri=http://%(site)s%(url)s&client_secret=%(secret)s&code=%(code)s'%{'id':APP_ID, 'secret':APP_SECRET, 'code':code, 'url': reverse('fblogin'),'site':current_site.domain}
        response = urllib2.urlopen(access_token_url)       
        html = response.read()
        parts = html.split('&')
        if len(parts) == 1:
            token = parts[0].split('=')[1]
            expiration = 50000
        elif len(parts) == 2:
            token = parts[0].split('=')[1]
            expiration = parts[1].split('=')[1]            
        config, created = FacebookConfig.objects.get_or_create(app_id=APP_ID,app_secret=APP_SECRET)
        config.access_token = token
        config.access_token_expiration = expiration
        config.updated_at = datetime.datetime.now()
        config.save()
        #graph.get_object('AitzolTest',fields="access_token")
        return HttpResponse('token: %(token)s expiration: %(expiration)s'% {'expiration': expiration, 'token': token})
