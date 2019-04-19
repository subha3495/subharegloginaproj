from django.db import models
class Reg(models.Model):
    user = models.CharField(primary_key=True, max_length=20)
    pwd=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    dob=models.DateField()
    mob=models.IntegerField()
    def __str__(self):
        return self.user