from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.




class ERRORCASE(models.Model):
    selecter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    error_01 = models.BooleanField(verbose_name='異常０１')
    error_02 = models.BooleanField(verbose_name='異常０２')
    error_03 = models.BooleanField(verbose_name='異常０３')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
