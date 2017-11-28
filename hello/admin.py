from django.contrib import admin

# Register your models here.

from .models import Question, Greeting

admin.site.register(Question)

admin.site.register(Greeting)