from django.db import models


# Not used

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
