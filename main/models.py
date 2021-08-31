from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.db.models.fields.related import ForeignKey

#Custom User Model
class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name,password, **other_fields):   
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assined to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assined to is_superuser=True')


        return self.create_user(email, user_name,password, **other_fields)

class Employee(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(null=True)
    user_name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)



    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)

    def __str__(self):
        return '{}'.format(self.name)



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    stock_quantity = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Requesition(models.Model):

    class Status(models.TextChoices):
        PENDING = 'A', 'PENDING'
        ACCEPTED = 'B', 'ACCEPTED'
        PARTIAL = 'C', 'PARTIALLY DELIVERED'
        DELIVERED = 'D', 'DELIVERED'

    id = models.AutoField(primary_key=True)
    requested_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Control_Number = models.CharField(max_length=50)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE)
    Item = models.ForeignKey(Product, on_delete=models.CASCADE)
    Qty = models.IntegerField()
    status = models.CharField(max_length=2,choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return self.Control_Number