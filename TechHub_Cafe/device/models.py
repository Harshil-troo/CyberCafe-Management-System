from django.db import models

ACTIVE = "active"
INACTIVE= "inactive"


USER_STATUS = [
    (ACTIVE,"ACTIVE"),
    (INACTIVE,"INACTIVE"),
]
class Computer(models.Model):
    computer_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    computer_name = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    ram = models.IntegerField()
    operating_system = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=USER_STATUS, default=ACTIVE)

    def __str__(self):
        return self.computer_name

