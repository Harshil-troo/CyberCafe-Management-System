from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


AADHAR = "aadhar"
PAN = "pan"
VOTER = "voter"

ID_TYPES = [
    (AADHAR,"AADHAR"),
    (PAN,"PAN"),
    (VOTER,"VOTER"),
]




class User(AbstractUser):

    class UserTypes(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        CUSTOMER = "CUSTOMER",_("Customer")


    user_type = models.CharField(choices=UserTypes)
    name = models.TextField(max_length=50)
    id_proof = models.CharField(max_length=20, choices=ID_TYPES,default="AADHAR")
    id_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer_name = models.ForeignKey("device.Computer", on_delete=models.CASCADE,related_name="name",null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):

        return f"{self.computer_name.computer_name}"