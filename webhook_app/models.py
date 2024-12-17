from django.db import models
import secrets
import uuid


# Create your models here.
class Accounts(models.Model):
    email_id=models.EmailField(unique=True,null=False)
    account_id=models.UUIDField(unique=True,null=False,default=uuid.uuid4)
    account_name=models.CharField(max_length=50,null=False)
    app_secret_token=models.CharField(max_length=50,editable=False,default=secrets.token_urlsafe)
    website=models.URLField(null=True,blank=True)
    
    class Meta:
        db_table="accounts"

class Destinations(models.Model):
    HTTP_METHOD_CHOICES=[("GET","GET"),("POST","POST"),("PUT","PUT")]
    account=models.ForeignKey(Accounts,related_name='destinations',on_delete=models.CASCADE)
    url=models.URLField(null=False)
    http_method=models.CharField(max_length=10,choices=HTTP_METHOD_CHOICES)
    headers=models.JSONField()

    class Meta:
        db_table="destinations"