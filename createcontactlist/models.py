from django.db import models


class CreateContactListData(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=170)
    location = models.CharField(max_length=170)
    designation = models.CharField(max_length=170)
    compName = models.CharField(max_length=170)

