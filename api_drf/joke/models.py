# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class JokeDuanzi(models.Model):
    title = models.CharField(max_length=30)
    nvum = models.PositiveIntegerField(blank=True, null=True)
    like_num = models.PositiveIntegerField(blank=True, null=True)
    no_like = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    is_hot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joke_duanzi'


class JokeImg(models.Model):
    img = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=30)
    nvum = models.PositiveIntegerField(blank=True, null=True)
    like_num = models.PositiveIntegerField(blank=True, null=True)
    no_like = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joke_img'
