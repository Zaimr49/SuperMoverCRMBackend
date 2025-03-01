from django.db import models

class APIIntegration(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()
    last_synced = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
