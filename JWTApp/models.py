from django.contrib.auth.hashers import make_password,is_password_usable,check_password
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(unique=True,null=True)
    city = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)