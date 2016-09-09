from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Assets(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    fgdzc = models.CharField(max_length=20)
    fname = models.CharField(max_length=50)
    fdate = models.DateTimeField(blank=True, null=True)
    fuser = models.CharField(max_length=50, blank=True, null=True)
    fdep = models.CharField(max_length=50)
    fip = models.GenericIPAddressField(blank=True, null=True)
    fdate_rz = models.DateField()
    fdate_bf = models.DateField(blank=True, null=True)
    smark = models.BooleanField(default=False)
    fstore = models.CharField(max_length=50, blank=True, null=True)
    fuserold = models.CharField(max_length=50, blank=True, null=True)
    f1 = models.CharField(max_length=30, blank=True, null=True)
    f2 = models.CharField(max_length=30, blank=True, null=True)
    fdate_ys = models.DateField(blank=True, null=True)
    fstate = models.ForeignKey(State, null=True)

    def __str__(self):
        return self.fgdzc
