Facebook Page Writer
====================

This is a little Django app for publishing in a Facebook page with the credentials of the page. FPW uses facebook-sdk library to post content and get credentials from facebook. 

Usage
=====

First we need to setup a app in facebook. It's important to set your url in the settings of the app.
Next we need to store de app_id and the app_secret in our settings.py_

FB_APP_ID=app_id
FB_APP_SECRET=app_secret

Once the app is set, we need to get the long term access_token. For that you have to access to the url in which you have installed FPW and login with your FB user (this user must have manage_page permision in the page you want to post)
FPW stores acces token and check expiration before posting. If access_token is expored, FPW sends a email to the ADMINS to recreate the token (so check the ADMIN seting and email sending)

Last you have to use the facebookpagewriter.utils.post method to post to the desired page.

facebookpagewriter.utils.post method
====================================

def post(page_id, component, message, **kwargs):

where:
   - page_id: the id of the page to post to. 
   - component: connection name to post in the page (feed, event..)
   - message: little message
   - kwargs must be attrs defined by facebook. Example, for the Post type: https://developers.facebook.com/docs/reference/api/post/
