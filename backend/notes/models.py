from django.db import models
from django.contrib.auth.models import User
from config.settings import base


class Tag(models.Model):
    ''' タグのテーブル '''
    name = models.CharField(max_length=50, verbose_name='タグ', unique=True)

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'


class Note(models.Model):
    ''' ノートのテーブル '''
    ''' 記事のテーブル '''
    DRAFT = 'DRAFT'
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'

    STATUS_CHOICES = [
        (DRAFT, '下書き'),
        (PUBLIC, '公開'),
        (PRIVATE, '非公開'),
    ]

    user = models.ForeignKey(
        base.AUTH_USER_MODEL, verbose_name='ユーザー名', on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200, verbose_name='タイトル',)
    content = models.TextField(verbose_name='本文')
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    status = models.CharField(
        max_length=10, verbose_name='ステータス', choices=STATUS_CHOICES, default=DRAFT)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ノート'
        verbose_name_plural = 'ノート'


class Comment(models.Model):
    ''' コメントのテーブル '''
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, verbose_name='ユーザー名', on_delete=models.CASCADE, related_name='comments')
    note = models.ForeignKey(
        Note, verbose_name='ノート', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='テキスト')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'


class Reply(models.Model):
    ''' 返信のテーブル '''
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, verbose_name='ユーザー名', on_delete=models.CASCADE, related_name='replies')
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, verbose_name='コメント', related_name='replies')
    text = models.TextField(verbose_name='テキスト',)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name = '返信'
        verbose_name_plural = '返信'


class Like(models.Model):
    ''' いいねのテーブル '''
    user = models.ForeignKey(
        base.AUTH_USER_MODEL, verbose_name='ユーザー名', on_delete=models.CASCADE, related_name='likes')
    note = models.ForeignKey(
        Note, verbose_name='ノート', on_delete=models.CASCADE, related_name='likes')
    added_at = models.DateTimeField(verbose_name='追加日時', auto_now_add=True)

    class Meta:
        verbose_name = 'いいね'
        verbose_name_plural = 'いいね'
