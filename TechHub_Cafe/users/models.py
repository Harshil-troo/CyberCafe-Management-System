from django.db import models
from django.contrib.auth.models import User



AADHAR = "aadhar"
PAN = "pan"
VOTER = "voter"

ID_TYPES = [
    (AADHAR,"AADHAR"),
    (PAN,"PAN"),
    (VOTER,"VOTER"),
]

USER_TYPES = [
    ("USER","USER"),
    ("ADMIN","ADMIN"),
]


class User(models.Model):
    user = models.OneToOneField(User,choices=USER_TYPES,on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    id_proof = models.CharField(max_length=20, choices=ID_TYPES,default="AADHAR")
    id_number = models.CharField(max_length=20)

    def __str__(self):

        return self.name

class Computer(models.Model):
    computer_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    computer_specifications = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.computer_id}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    computer_id = models.ForeignKey(Computer, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):

        return f"{self.computer_id.computer_id}"