# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

'''
class TbUsr(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_name_reference = models.CharField(unique=True, max_length=20)
    usr_pw = models.CharField(max_length=20)

    def __str__(self):
        return self.usr_name_reference

    class Meta:
        managed = True
        db_table = 'tb_usr'

'''

class TbUsrDev(models.Model):
    usr_dev_id = models.AutoField(primary_key=True)
    usr_name_foreign = models.ForeignKey(User, models.DO_NOTHING, db_column='usr_name_foreign')
    dev_name_reference = models.CharField(unique=True, max_length=4)

    class Meta:
        managed = True
        db_table = 'tb_usr_dev'

    #若存在dev_name_foreign的选项是从父表此处返回的
    def __str__(self):
        return self.dev_name_reference

class TbDev(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name_foreign = models.ForeignKey(TbUsrDev, models.DO_NOTHING, db_column='device_name_foreign')
    device_intodepot_time = models.DateTimeField()
    device_location_mode = models.IntegerField(blank=True, null=True)
    device_batter_lowpower = models.IntegerField()
    device_batter_level = models.FloatField()
    device_location_gps_longitude = models.FloatField(blank=True, null=True)
    device_location_gps_latitude = models.FloatField(blank=True, null=True)
    device_location_gps_altitude = models.FloatField(blank=True, null=True)
    device_location_gps_speed = models.FloatField(blank=True, null=True)
    device_location_gps_longitude_direction = models.IntegerField(blank=True, null=True)
    device_location_gps_latitude_direction = models.IntegerField(blank=True, null=True)
    device_location_gps_altitude_direction = models.IntegerField(blank=True, null=True)
    device_location_wifi_mac = models.CharField(max_length=20, blank=True, null=True)
    device_location_lbs_movecityid = models.CharField(max_length=4, blank=True, null=True)
    device_location_lbs_locationid = models.CharField(max_length=4, blank=True, null=True)
    device_location_lbs_villageid = models.CharField(max_length=4, blank=True, null=True)
    device_location_lbs_movenetid = models.CharField(max_length=4, blank=True, null=True)
    device_location_publish_intervaltime = models.CharField(max_length=2, blank=True, null=True)
    device_location_publish_phonenumber = models.CharField(max_length=26, blank=True, null=True)
    device_payload = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_dev'
    #暂时没用到此处的返回
    def __str__(self):
        return self.device_name_foreign_id