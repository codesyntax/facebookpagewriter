from django.db import models

class FacebookConfig(models.Model):
    app_id = models.CharField(max_length=40)
    app_secret = models.CharField(max_length=120)
    access_token = models.CharField(max_length=255)
    access_token_expiration = models.PositveField()
    updated_at = models.DateTimeField()
    
