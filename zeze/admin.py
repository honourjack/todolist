# zeze/admin.py

from django.contrib import admin
from .models import Profile, Task, Tag

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Tag)
