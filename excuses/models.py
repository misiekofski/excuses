from django.db import models

# Create your models here.

class RootCause(models.Model):
    cause_text = models.CharField(max_length=500)
    def __str__(self):
        return self.cause_text