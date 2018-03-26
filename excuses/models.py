from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bug(models.Model):
    bug_description = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bug_description


class RootCause(models.Model):
    bug = models.ForeignKey(Bug, related_name='rootcause',on_delete=models.CASCADE)
    cause_text = models.CharField(max_length=500)

    def __str__(self):
        return self.cause_text

class ActionPlan(models.Model):
    rootcause = models.ForeignKey(RootCause, related_name='actionplan',on_delete=models.CASCADE)
    action_text = models.CharField(max_length=500)

    def __str__(self):
        return self.action_text