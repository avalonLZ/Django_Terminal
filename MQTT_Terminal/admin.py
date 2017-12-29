# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from MQTT_Terminal.models import TbDev
#from MQTT_Terminal.models import TbUsr
from MQTT_Terminal.models import TbUsrDev
'''
#注意有主从键关系时，一定要注意注册的先后顺序
def usr_name_reference(obj):
    return obj.usr_name_reference
usr_name_reference.short_description = u'用户'

class TbUsr_Admin(admin.ModelAdmin):
    list_display = (usr_name_reference, )

admin.site.register(TbUsr, TbUsr_Admin)

'''

def usr_name_foreign(obj):
    return obj.usr_name_foreign_id#注意使用外键一定要加id
usr_name_foreign.short_description = u'用户'

def dev_name_reference(obj):
    return obj.dev_name_reference
dev_name_reference.short_description = u'设备名'

class TbUsrDev_Admin(admin.ModelAdmin):
    #列表显示以下两字段
    list_display = (dev_name_reference, usr_name_foreign, )

admin.site.register(TbUsrDev, TbUsrDev_Admin)



def dev_name(obj):
    return obj.device_name_foreign_id
dev_name.short_description = u'设备名'

def dev_intodepot_time(obj):
    return obj.device_intodepot_time
dev_intodepot_time.short_description = u'录入时间'

def dev_location_mode(obj):
    return obj.device_location_mode
dev_location_mode.short_description = u'定位方式'

def dev_batter_lowpower(obj):
    return obj.device_batter_lowpower
dev_batter_lowpower.short_description = u'是否低压'

def dev_batter_level(obj):
    return obj.device_batter_level
dev_batter_level.short_description = u'电池电量'

def dev_location_gps_longitude(obj):
    return obj.device_location_gps_longitude
dev_location_gps_longitude.short_description = u'经度'

def dev_location_gps_latitude(obj):
    return obj.device_location_gps_latitude
dev_location_gps_latitude.short_description = u'纬度'

def dev_location_gps_altitude(obj):
    return obj.device_location_gps_altitude
dev_location_gps_altitude.short_description = u'高度'

def dev_location_gps_speed(obj):
    return obj.device_location_gps_speed
dev_location_gps_speed.short_description = u'速度'

def dev_location_wifi_mac(obj):
    return obj.device_location_wifi_mac
dev_location_wifi_mac.short_description = u'MAC地址'

def dev_location_lbs_movecityid(obj):
    return obj.device_location_lbs_movecityid
dev_location_lbs_movecityid.short_description = u'移动国家码'

def dev_location_lbs_locationid(obj):
    return obj.device_location_lbs_locationid
dev_location_lbs_locationid.short_description = u'本地编码'

def dev_location_lbs_villageid(obj):
    return obj.device_location_lbs_villageid
dev_location_lbs_villageid.short_description = u'小区ID'

def dev_location_lbs_movenetid(obj):
    return obj.device_location_lbs_movenetid
dev_location_lbs_movenetid.short_description = u'移动网络ID'

def dev_location_publish_intervaltime(obj):
    return obj.device_location_publish_intervaltime
dev_location_publish_intervaltime.short_description = u'上报时间间隔'

def dev_location_publish_phonenumber(obj):
    return obj.device_location_publish_phonenumber
dev_location_publish_phonenumber.short_description = u'亲情号码'

def dev_payload(obj):
    return obj.device_payload
dev_payload.short_description = u'有效载荷'


class TbDev_Admin(admin.ModelAdmin):
    list_display = (dev_name, dev_intodepot_time, dev_location_mode,
                    dev_batter_lowpower, dev_batter_level, dev_location_gps_longitude,
                    dev_location_gps_latitude, dev_location_gps_altitude, dev_location_gps_speed,
                    dev_location_wifi_mac, dev_location_lbs_movecityid, dev_location_lbs_locationid,
                    dev_location_lbs_villageid, dev_location_lbs_movenetid, dev_location_publish_intervaltime,
                    dev_location_publish_phonenumber, dev_payload, )

admin.site.register(TbDev, TbDev_Admin)

