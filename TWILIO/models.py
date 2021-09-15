from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.conf import settings


class CUSTOMUSER(AbstractUser):
    Phone_No = models.CharField(max_length=50) 

    def __str__(self):
        return self.username 

class CODE(models.Model): 
    user = models.OneToOneField(CUSTOMUSER, on_delete=models.CASCADE)
    Number_Code = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.Number_Code) 
        

    def save(self, *args, **kwargs):
        number_list = [y for y in range(10)]
        code_items = []
        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.Number_Code = code_string
        super().save(*args, **kwargs)