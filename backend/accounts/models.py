from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(verbose_name='プロフ画像',
                                        upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(verbose_name='自己紹介文', null=True, blank=True)
    birthdate = models.DateField(verbose_name='生年月日', null=True, blank=True)
    following = models.ManyToManyField(
        'self', verbose_name='フォロー', related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'アカウント'
        verbose_name_plural = 'アカウント'
