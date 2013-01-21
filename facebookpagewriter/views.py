import hashlib
import random
import string
import urllib2
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings

APP_ID = getattr(settings, 'FB_APP_ID')
APP_SECRET = getattr(settings, 'FB_APP_SECRET')

def fblogin(request):
    if 'code' not in request.GET:
        state = hashlib.sha224(''.join(random.sample(string.printable,40))).hexdigest()
        dialog_url = "https://www.facebook.com/dialog/oauth?client_id=%(id)s&redirect_uri=http://beta.niagarank.local%(url)s&state=%(state)s&scope=publish_actions,status_update,publish_stream,manage_pages" % {'id':APP_ID,'state': state, 'url': reverse('nrgk_fblogin')}
        return HttpResponseRedirect(dialog_url)
    else:
        #state = request.GET['state']
        code = request.GET['code']
        access_token_url = 'https://graph.facebook.com/oauth/access_token?client_id=%(id)s&redirect_uri=http://beta.niagarank.local%(url)s&client_secret=%(secret)s&code=%(code)s'%{'id':APP_ID, 'secret':APP_SECRET, 'code':code, 'url': reverse('nrgk_fblogin')}
        response = urllib2.urlopen(access_token_url)       
        html = response.read()
        token, expiration = html.split('&')
        token = token.split('=')[1]
        expiration = expiration.split('=')[1]
        #graph.get_object('AitzolTest',fields="access_token")
        return HttpResponse('token: %(token)s expiration: %(expiration)s'% {'expiration': expiration, 'token': token})
