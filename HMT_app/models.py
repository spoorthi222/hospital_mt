# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StaffTable(models.Model):
    id     =models.AutoField(primary_key=True)
    name   =models.CharField(max_length=50,default="N/A")
    desig   =models.CharField(max_length=40)
    s_scale =models.CharField(max_length=7,default="N/A")


    def save(self,*args,**kwargs):
        return super(StaffTable,self).save(*args,**kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table  = 'staff_table_1'
        app_label = 'HMT_app'