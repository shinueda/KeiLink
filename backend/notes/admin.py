from django.contrib import admin
from .models import Note, Comment, Reply, Like, Tag

admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Like)
admin.site.register(Tag)
