from django.db import models

class Users(models.Model):
    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=50, default="")
    email_id = models.CharField(max_length=100,default="")
    phone_no = models.CharField(max_length=7, default="")


    def save(self,*args,**kwargs):
        return super(Users,self).save(*args,**kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table  = 'users'
        app_label = 'src'