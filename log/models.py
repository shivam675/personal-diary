from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class MyLogEntry(models.Model):

    created     = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    intresting = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.created)
    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.modified = timezone.now()
    #     return super(log_entries, self).save(*args, **kwargs)
