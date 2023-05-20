from django.contrib import admin
from .models import Note, Comment, Reply, Like, Tag


class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'note', 'text', 'created_at')


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'text', 'created_at')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'note', 'added_at')


class TagAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at')


admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Tag, TagAdmin)
