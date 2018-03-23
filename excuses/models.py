from django.db import models

# Create your models here.

class RootCause(models.Model):
    cause_text = models.CharField(max_length=500)
    def __str__(self):
        return self.cause_text

class ActionPlan(models.Model):
    rootcause = models.ForeignKey(RootCause, related_name='actionplan',on_delete=models.CASCADE)
    action_text = models.CharField(max_length=500)

    def __str__(self):
        return self.action_text