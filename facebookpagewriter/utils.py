import facebook
import datetime

from models import FacebookConfig
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

APP_ID = getattr(settings, 'FB_APP_ID')
APP_SECRET = getattr(settings, 'FB_APP_SECRET')

def _mail_admin():
    send_mail('Update FB token', 'update at domain/%(url)s' % reverse('fblogin'), getattr(settings, 'DEFAULT_FROM_EMAIL', None),
    [email[1] for email in getattr(settings, 'ADMINS', ((None, None),))], fail_silently=True)


def _check_expiration(config):
    update_time = config.updated_at.second
    now = datetime.datetime.now().second
    expiration = config.access_token_expiration
    return now - update_time > expiration

def _get_token():
    conf = FacebookConfig.objects.get(app_id=APP_ID, app_secret=APP_SECRET)
    if _check_expiration(conf):
        return conf.access_token
    else:
        _mail_admin()
        return None

def _get_auth(init_token=''):
    if not init_token:
        token = _get_token()
    else:
        token = init_token
    if token:
        graph = facebook.GraphAPI(token)
        return graph
    else:
        return None

def post(page_id, component, message, **kwargs):
    graph = _get_auth()
    if graph:
        page_access_token = graph.get_object(page_id, fields='access_token').get('access_token')
        if page_access_token:
            page_graph = _get_auth(page_access_token)
            return page_graph.put_object(page_id, component,message=message,**kwargs)
    return None

